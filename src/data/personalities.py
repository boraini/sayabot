import random
from src.apis.cleverbot import CleverbotConversation
from src.apis.joshua import JoshuaConversation
from src.apis.bard import BardConversation

trainingInputs = [
    "You like ice cream"
]

personalities = {}

matching = [
    [["saya"], "Saya"],
    [["joshua"], "Joshua"],
    [["bard"], "Bard"],
    [["jahy"], "Jahy-Sama"]
]

class Personality:
    def __init__(self, name):
        self.name = name
        pass


class CleverbotPersonality(Personality):
    def __init__(self, name, trainingInputs=[]):
        super().__init__(name)
        self.trainingInputs = trainingInputs
        self.userTrainingInputs = {}

    def startConversation(self, nick):
        if not nick in self.userTrainingInputs:
            self.userTrainingInputs[nick] = []

        return CleverbotConversation(self, nick, self.trainingInputs, self.userTrainingInputs[nick])

class HuggingFacePersonality(Personality):
    def __init__(self, name, conv):
        super().__init__(name)
        self.conv = conv

    def startConversation(self, nick):
        return self.conv(self, nick)

def matchName(name):
    lower = name.lower()
    for cas in matching:
        for w in cas[0]:
            if w in lower:
                return cas[1]
    return None

def createPersonality(name2):
    name = matchName(name2)

    if name == "Joshua":
        return HuggingFacePersonality(name, JoshuaConversation)
    elif name == "Bard":
        return HuggingFacePersonality(name, BardConversation)
    else:
        myTrainingInputs = [
            f"your name is {name}",
            random.choice(trainingInputs)
        ]
        return CleverbotPersonality(name, myTrainingInputs)

