from .data import personalities

""" dictionary to hold all conversations keyed by Discord handles """
conversations = {}

personalities.personalities["Saya"] = personalities.createPersonality("Saya")
personalities.personalities["Joshua"] = personalities.createPersonality("Joshua")
personalities.personalities["Bard"] = personalities.createPersonality("Bard")

async def handleDDTalk(message, messageStr):
    rest = messageStr
    nickPrefix = ""
    if not str.strip(rest):
        return nickPrefix + "You need to either provide a character name or a nonempty message in case you are in a conversation."
    if message.author in conversations:
        if rest == "end":
            await conversations[message.author].end()
            del conversations[message.author]
            return nickPrefix + "Conversation ended successfully."
        else:
            return nickPrefix + await conversations[message.author].sendMessage(rest)
    else:
        name = personalities.matchName(rest)
        if name in personalities.personalities:
            conversations[message.author] = personalities.personalities[name].startConversation(message.author)
            return nickPrefix + "Conversation started successfully."
        else:
            return nickPrefix + f"There is no one called {rest} who I know of."