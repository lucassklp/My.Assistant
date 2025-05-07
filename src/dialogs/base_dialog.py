from intents import IntentData

class BaseDialog:
    intent: IntentData
    def process(self):
        """
        Process the dialog.
        """
        raise NotImplementedError("Subclasses must implement this method")
