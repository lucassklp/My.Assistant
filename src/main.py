from dialogs.wake_up_word_dialog import WakeUpWordDialog
from stt import listen
import tts
from intents import Intent, get_intent

try:
    while True:
        fala = listen()
        intent = get_intent(fala)
        if intent.matches(Intent.WAKE_UP_WORD):
            dialog = WakeUpWordDialog()
            dialog.process()

except KeyboardInterrupt:
    print("\nConcluído")
except Exception as e:
    print("um erro aconteceu: " + str(e))

