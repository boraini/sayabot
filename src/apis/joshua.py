import requests
import json
from .huggingface import HuggingFaceConversation

apis = {
    "Joshua": "https://api-inference.huggingface.co/models/ThatSkyFox/DialoGPT-small-joshua"
}

class JoshuaConversation(HuggingFaceConversation):
    def __init__(self, personality, nick):
        super().__init__(personality, nick)
        
        self.apiURL = apis[personality.name]
        self.inputs = {
            "past_user_inputs": [],
            "generated_responses": [],
            "text": ""
        }
    
    def getTutorial(self):
        return "Hi. I am Joshua from the visual novel *The World Ends With You.*"
    
    async def sendMessage(self, message):
        if message == "":
            return None

        self.inputs["text"] = message
            
        response = self.makeRequest({
            "inputs": self.inputs
        })

        if type(response) == str:
            return response

        responseError = self.detectResponseError(response)

        if not responseError == None:
            return responseError

        self.inputs["past_user_inputs"] = response["conversation"]["past_user_inputs"]
        self.inputs["generated_responses"] = response["conversation"]["generated_responses"]

        if len(self.inputs["past_user_inputs"]) >= 4:
            self.inputs["past_user_inputs"].pop(0)
            self.inputs["generated_responses"].pop(0)
        return self.nickPrefix + response["generated_text"]