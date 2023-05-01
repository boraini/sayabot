import disnake
import asyncio
from disnake.ext import commands
from .DummyMessage import DummyMessage

from . import ddtalk as DDTalk
from .apis.huggingface import setupHuggingFace

command_sync_flags = commands.CommandSyncFlags.default()
command_sync_flags.sync_commands_debug = True

def main(env, noDiscord):
  TOKEN = env["DISCORD_TOKEN"]
  GUILD_ID = int(env["GUILD_ID"])
  setupHuggingFace(token=env["HUGGINGFACE_TOKEN"])

  client = commands.Bot(
    command_prefix="!",
    test_guilds=[GUILD_ID],
    intents=disnake.Intents(message_content=True, messages=True),
    command_sync_flags=command_sync_flags,
  )

  @client.slash_command(description="Responds with 'beep bop'")
  async def ddtest(ctx):
    await ctx.send('you haram boy stop simping for anime girls /nf')
    
  @client.slash_command(pass_context=True, description="Talk to someone")
  async def ddtalk(interaction, message : str):
    await interaction.response.defer()
    res = await DDTalk.handleDDTalk(interaction, message)

    if res != None:
      await interaction.followup.send(f"> {message}\n{res}")

  async def noDiscordLoop():
    while True:
      msg = input()
      message = DummyMessage(msg)
      await ddtalk(message.interaction, msg)

  if noDiscord:
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    try:
        loop.run_until_complete(noDiscordLoop())
    finally:
        loop.run_until_complete(loop.shutdown_asyncgens())
        loop.close()
      
  else:
    client.run(TOKEN)