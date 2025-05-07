import queue
import sys
import sounddevice as sd
from vosk import Model, KaldiRecognizer, SetLogLevel
import json

print("Inicializando o reconhecimento de fala...")

q = queue.Queue()
model = Model(lang="pt")
device_info = sd.query_devices(None, "input")
samplerate = int(device_info["default_samplerate"])

rec = KaldiRecognizer(model, samplerate)
SetLogLevel(-2)

channels = 1
blocksize = 8000


print("Reconhecimento de fala iniciado com os parametros: samplerate = " + str(samplerate) + ", blocksize=" + str(blocksize) + ", channels = " + str(channels))

def callback(indata, frames, time, status):
    """This is called (from a separate thread) for each audio block."""
    if status:
        print("Erro ao incluir na fila: " + str(status), file=sys.stderr)
    q.put(bytes(indata))

def listen():
    with sd.RawInputStream(samplerate=samplerate, blocksize = blocksize, dtype="int16", channels=channels, callback=callback):
        while True:
            data = q.get()
            if rec.AcceptWaveform(data):
                result = json.loads(rec.Result())
                text = result['text']
                with q.mutex:
                    q.queue.clear()
                if text != "":
                    print("Fala reconhecida: " + text)
                    return text
                else:
                    print("Nenhuma fala reconhecida, tentando novamente...")
            else:
                result = json.loads(rec.PartialResult())
                print("Parcial: " + result['partial'])


