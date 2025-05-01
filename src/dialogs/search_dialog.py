from dialogs.base_dialog import BaseDialog
import openai
from tts import speak_sequence
import asyncio
import os

client = openai.OpenAI(api_key = os.getenv("OPEN_API_KEY"))

class SearchDialog(BaseDialog):

    def __init__(self, intent):
        """
        Initialize the SearchDialog.
        :param intent: The intent to process.
        """
        self.intent = intent

    def process(self):
        asyncio.run(speak_sequence(["Estou pesquisando para você, aguarde um momento!"]))
        response = client.responses.create(
            model="gpt-4.1",
            input=self.intent.utterance,
            instructions="Retorne apenas o texto limpo, sem formatação, sem tags html ou markdown. Não retorne nada além do texto. Não retorne listas, apenas texto corrido.",
        )
        texto = response.output_text
        print("Texto obtido pelo chatgpt: " + texto)
        asyncio.run(speak_sequence(texto.split(".")))

