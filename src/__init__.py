import disnake
from disnake.ext import commands

from . import ddtalk as DDTalk

command_sync_flags = commands.CommandSyncFlags.default()
command_sync_flags.sync_commands_debug = True

client = commands.Bot(
command_prefix="!",
test_guilds=[],
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
  
  
def main(env, noDiscord):
  TOKEN = env["DISCORD_TOKEN"]
  
  if noDiscord:
    pass
  else:
    client.run(TOKEN)