import random
from src.apis.cleverbot import CleverbotConversation
from src.apis.huggingface import HuggingFaceConversation

trainingInputs = [
    "You like ice cream"
]

personalities = {}

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
    def __init__(self, name):
        super().__init__(name)

    def startConversation(self, nick):
        return HuggingFaceConversation(self, nick)

def createPersonality(name):

    if name == "Joshua":
        return HuggingFacePersonality(name)
    else:
        myTrainingInputs = [
            f"your name is {name}",
            random.choice(trainingInputs)
        ]
        return CleverbotPersonality(name, myTrainingInputs)

