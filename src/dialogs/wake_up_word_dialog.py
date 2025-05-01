import os
from dialogs.base_dialog import BaseDialog
from dialogs.search_dialog import SearchDialog
from intents import Intent, IntentData, get_intent
from tts import speak_sequence
from stt import listen

class WakeUpWordDialog(BaseDialog):

    def get_dialog(self, intent) -> BaseDialog:
        """
        Get the dialog for the intent.
        :param intent: The intent to get the dialog for.
        :return: The dialog for the intent.
        """
        if intent in self.dialogs:
            return self.dialogs[intent]
        else:
            raise ValueError("Dialog not found for intent: " + str(intent))

    def process(self):
        print("Processando dialogo de wake up word")
        os.system("aplay confirm.wav")
        fala = listen()
        intent = get_intent(fala)
        if intent.matches(Intent.UNRECOGNIZED):
            speak_sequence(["Desculpe, não entendi o que você disse."
                            "Devo pesquisar sobre" + intent.utterance + "?"])
            intent = get_intent(fala)
            if intent.matches(Intent.YES):
                dialog = SearchDialog(IntentData(Intent.SEARCH, [], fala))
                dialog.process()
        elif intent.matches(Intent.SEARCH):
            dialog = SearchDialog(intent)
            dialog.process()
            

