from .data import personalities

""" dictionary to hold all conversations keyed by Discord handles """
conversations = {}

personalities.personalities["Saya"] = personalities.createPersonality("Saya")
personalities.personalities["Joshua"] = personalities.createPersonality("Joshua")

async def handleDDTalk(message, messageStr):
    rest = messageStr
    print(messageStr)
    if not str.strip(rest):
        return nickPrefix + "You need to either provide a character name or a nonempty message in case you are in a conversation."
    nickPrefix = f"[to {message.author}] "
    if message.author in conversations:
        if rest == "end":
            await conversations[message.author].end()
            del conversations[message.author]
            return nickPrefix + "Conversation ended successfully."
        else:
            return nickPrefix + await conversations[message.author].sendMessage(rest)
    else:
        if rest in personalities.personalities:
            conversations[message.author] = personalities.personalities[rest].startConversation(message.author)
            return nickPrefix + "Conversation started successfully."
        else:
            return nickPrefix + f"There is no one called {rest} who I know of."