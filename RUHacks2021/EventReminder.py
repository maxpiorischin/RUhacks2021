import discord
from discord.ext import commands
import os

token = os.getenv("EVENT_REMINDER_TOKEN")

if __name__ == '__main__':
    client = commands.Bot(command_prefix= "-")


    @client.event
    async def on_ready():
        members = 0
        for guild in client.guilds:
            members += guild.member_count
        await client.change_presence(status=discord.Status.online,
                                     activity=discord.Activity(type=discord.ActivityType.watching,
                                                               name=f"{members} users!"))
        print("Event reminder is ready!")


    @client.command()
    async def load(ctx, extension):
        client.load_extension(f"cogs.{extension}")


    @client.command()
    async def unload(ctx, extension):
        client.unload_extension(f"cogs.{extension}")


    print("-------------------")
    for cog in os.listdir("./cogs"):
        if cog.endswith(".py"):
            try:
                client.load_extension(f"cogs.{cog[:-3]}")
                print(f"{cog} Loaded!")
            except Exception as e:
                print(f"{cog} cannot be loaded:")
                raise e
    print("-------------------")

    client.run(token)