class CleverbotConversation:
    def __init__(self, personality, nick, trainingInputs, userTrainingInputs):
        self.trainingInputs = trainingInputs
        self.userTrainingInputs = userTrainingInputs

    async def sendMessage(self, message):
        output = []
        output.append("Here is a description of me:")
        output.append("- " + "\n- ".join(self.trainingInputs))
        output.append("so shut up")
        return "\n".join(output)

    async def end(self):
        pass