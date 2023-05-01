class DummyAuthor:
    def __init__(self):
        self.name = "Olivia"

author = DummyAuthor()

class DummyResponse:
    async def defer(self):
        pass

class DummyFollowup:
    def __init__(self, message):
        self.message = message

    async def send(self, msg):
        self.message.interaction.send(msg)

class DummyInteraction:
    def __init__(self, message):
        self.followup = DummyFollowup(message)
        self.author = author
        self.response = DummyResponse()

    def send(self, msg):
        print(msg)

class DummyMessage:
    def __init__(self, message):
        self.message = message
        self.interaction = DummyInteraction(self)

        