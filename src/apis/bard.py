from .huggingface import HuggingFaceConversation

apis = {
    "Bard": "https://api-inference.huggingface.co/models/distilgpt2"
}

class BardConversation(HuggingFaceConversation):
    def __init__(self, personality, nick):
        super().__init__(personality, nick)

        self.apiURL = apis[personality.name]
        self.inputs = ""
        self.pastInputs = []

    def getTutorial(self):
        return "Write your story together with The Bard!"

    async def sendMessage(self, message):
        if message == "":
            return None

        self.pastInputs.append(message)

        if len(self.pastInputs) > 3:
            self.pastInputs.pop(0)

        self.inputs = "".join(self.pastInputs)
        
        responseArray = self.makeRequest({
            "inputs": self.inputs
        })

        if type(responseArray) == str:
            return responseArray

        response = responseArray
        
        if type(responseArray) == list:
            response = responseArray[0]

        responseError = self.detectResponseError(response)

        if not responseError == None:
            return responseError

        return self.nickPrefix + response["generated_text"]