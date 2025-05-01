from enum import Enum
import re

class Intent(Enum):
    UNRECOGNIZED = -1
    WAKE_UP_WORD = 0
    PLAY = 1
    SEARCH = 2
    RUN = 3
    YES = 4
    NO = 5

class IntentData:
    parameters = []
    intent = None
    utterance = ""
    def __init__(self, intent, parameters, utterance):
        self.intent = intent
        self.parameters = parameters
        self.utterance = utterance
    
    def matches(self, intent):
        return self.intent == intent


dictionary = {
    Intent.WAKE_UP_WORD: [re.compile(r"testando"), re.compile(r"estando")],
    Intent.PLAY: [],
    Intent.SEARCH: [ re.compile(r"(pesquise|pesquise sobre)([\w ]*)") ],
    Intent.RUN: [],
    Intent.YES: [re.compile(r"(sim|claro|com certeza|pode ser|pode)"), re.compile(r"ok")],
    Intent.NO: [re.compile(r"(não|de jeito nenhum|de forma alguma|nem pensar|nunca)")],
}

def get_intent(utterance: str) -> IntentData:
    """
    Get the intent of the utterance.
    :param utterance: The utterance to get the intent from.
    :return: The intent of the utterance.
    """
    print("Procurando intent para a frase: " + utterance)
    for intent, regexes in dictionary.items():
        for regex in regexes:
            if regex.match(utterance):
                intentData = IntentData(intent, [], utterance)
                print("Intent encontrada: " + str(intent))
                return intentData
    print("Nenhum intent encontrado para a frase: " + utterance)
    return IntentData(Intent.UNRECOGNIZED, [], utterance)