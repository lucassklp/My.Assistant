from piper import PiperVoice
import wave
import os
import tempfile
import asyncio
from functools import partial
from concurrent.futures import ThreadPoolExecutor

executor = ThreadPoolExecutor()

current_path = os.path.dirname(os.path.abspath(__file__))

print("Carregando os modelos de voz")
voice = PiperVoice.load(current_path + "/models/pt_BR-faber-medium.onnx",
    config_path=current_path + "/models/pt_BR-faber-medium.onnx.json",
    use_cuda=False
)

print("Modelo carregado com sucesso")

synthesize_args = {
    "sentence_silence": 0.0
}

def speak(text):
    asyncio.run(speak_sequence([text]))

def sintetizar_para_arquivo(text, filename):
    with wave.open(filename, "wb") as wav_file:
        voice.synthesize(text, wav_file, **synthesize_args)

async def sintetizar_async(text):
    tmp = tempfile.NamedTemporaryFile(delete=False, suffix=".wav")
    filename = tmp.name
    tmp.close()  # fechar antes de usar wave
    await asyncio.get_event_loop().run_in_executor(
        executor, partial(sintetizar_para_arquivo, text, filename)
    )
    return filename

async def tocar_audio(filename):
    print(f"Tocando: {filename}")
    process = await asyncio.create_subprocess_exec("aplay", filename)
    await process.communicate()
    os.remove(filename)

async def speak_sequence(text_list):
    if not text_list:
        return

    # Sintetiza o primeiro antes de começar
    current_audio = await sintetizar_async(text_list[0])

    for next_text in text_list[1:]:
        # Começa a sintetizar o próximo enquanto toca o atual
        next_audio_future = asyncio.create_task(sintetizar_async(next_text))
        await tocar_audio(current_audio)
        current_audio = await next_audio_future

    # Toca o último que ficou pendente
    await tocar_audio(current_audio)
