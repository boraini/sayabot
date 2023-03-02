import requests
import json

HUGGINGFACE_TOKEN = None
headers = None

apis = {
    "Joshua": "https://api-inference.huggingface.co/models/ThatSkyFox/DialoGPT-small-joshua"
}

def setupHuggingFace(**kwargs):
    HUGGINGFACE_TOKEN = kwargs["token"]
    headers = {"Authorization": f"Bearer {HUGGINGFACE_TOKEN}"}

class HuggingFaceConversation:
    def __init__(self, personality, nick):
        self.personalityName = personality.name
        self.nickPrefix = f"[{personality.name}] "
        self.apiURL = apis[personality.name]
        self.inputs = {
            "past_user_inputs": [],
            "generated_responses": [],
            "text": ""
        }
    
    async def sendMessage(self, message):
        if message == "":
            return None
        self.inputs["text"] = message
        try:
            res = requests.post(self.apiURL, headers=headers, json={
                "inputs": self.inputs
            }, timeout=4)
        except(requests.exceptions.Timeout):
            return self.nickPrefix + "HuggingFace was too slow to complete your request."
        response = json.loads(res.content.decode('utf-8'))
        print(response)
        if not "generated_text" in response:
            if "error" in response:
                if "currently loading" in response["error"]:
                    return f"Please give some time for {self.personalityName} to wake up, around {response['estimated_time']} seconds."
            
                return f"I don't know what it means but {self.personalityName} said they have this problem: {response['error']}"
            return f"Uuh, something is wrong with {self.personalityName}, I can feel it."
        print(self.inputs)
        self.inputs["past_user_inputs"] = response["conversation"]["past_user_inputs"]
        self.inputs["generated_responses"] = response["conversation"]["generated_responses"]
        if len(self.inputs["past_user_inputs"]) >= 4:
            self.inputs["past_user_inputs"].pop(0)
            self.inputs["generated_responses"].pop(0)
        print(self.inputs)
        return self.nickPrefix + response["generated_text"]

    async def end(self):
        pass
