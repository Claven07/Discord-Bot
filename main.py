from discord_components import ComponentsBot

from music_cog import music_cog

bot = ComponentsBot(command_prefix = '!')

bot.add_cog(music_cog(bot))

with open('token.txt', 'r') as file:
    token = file.readlines()(0)
bot.run(token)