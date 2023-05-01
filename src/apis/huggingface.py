import requests
import json

HUGGINGFACE_TOKEN = None
globalData = {
    "headers": {"Authorization": f"Bearer 00000000000000000000"}
}

def setupHuggingFace(**kwargs):
    HUGGINGFACE_TOKEN = kwargs["token"]
    globalData["headers"] = {"Authorization": f"Bearer {HUGGINGFACE_TOKEN}"}

class HuggingFaceConversation:
    def __init__(self, personality, nick):
        self.globalData = globalData
        self.personalityName = personality.name
        self.nickPrefix = ""

    def makeRequest(self, obj):
        try:
            res = requests.post(self.apiURL, headers=globalData["headers"], json={
                "inputs": self.inputs
            }, timeout=30)
        except(requests.exceptions.Timeout):
            return "HuggingFace was too slow to complete your request."
        
        response = json.loads(res.content.decode('utf-8'))

        return response

    def detectResponseError(self, response):
        if not "generated_text" in response:
            if "error" in response:
                if "currently loading" in response["error"]:
                    return f"Please give some time for {self.personalityName} to wake up, around {response['estimated_time']} seconds."
            
                return f"I don't know what it means but {self.personalityName} said they have this problem: {response['error']}"
            return f"Uuh, something is wrong with {self.personalityName}, I can feel it."
        else:
            return None

    async def end(self):
        pass