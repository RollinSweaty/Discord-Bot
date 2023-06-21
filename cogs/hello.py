import discord
import random
from discord.ext import commands


class Hello(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        print("Hello cog loaded.")

    @commands.Cog.listener()
    async def on_ready(self):
        print("Bot is alive")

    @commands.command()
    async def hello(self, ctx):
        await ctx.send("Hello Gamer! Bot is here for you")

    @commands.command()
    async def bot(self, ctx):
        await ctx.send("Im Bot")

    @commands.command()
    async def nightmares(self, ctx):
        await ctx.send("Ask me what I do for a living?")

    @commands.command()
    async def help(self, ctx):
        await ctx.send("Hello Gamer! Bot is here for you, here is a list of my commands, hello, rules, bot, nightmares, drifter, cayde, gamer, wholesome")

    @commands.command()
    async def rules(self, ctx):
        await ctx.send("Hello Gamer! Bot says be a good person or else")

    @commands.command()
    async def drifter(self, ctx):
        quotes = ["Enough foolin' around!", "Drifter's hungry!",
                  "All right, mavericks! Ready to see what you're fightin' today?",
                  "All right, all right, all right. Let's see what we've got.",
                  "Yeah, I was at Twilight Gap. My grandma, too. Who wasn't? Shoot some Fallen!",
                  "If you see one Hive soldier, a hundred more are waiting for you that you don't see--yet.",
                  "Think you could eat a Hive knight? Those're the questions you ask yourself on the frontier.",
                  "I've dealt with ugly, but damn! Scorn are UGLY! Finish this fast, yeah?",
                  "Fallen. ...I'd go out there with ya, but I pawned my Gjallarhorn. Shucks.",
                  "Ever been up to the Leviathan? Cabal can be a HOOT! Still gotta fight'em.",
                  "Cabal culture is all military these days. Used to be they were easier to kill.",
                  "You can burn Hive guts for a fire in the wild. It's toasty!",
                  "It takes about a hundred of Shaxx's Redjacks to take down a Hive Knight. Why does he bother building'em?",
                  "Ever pull a gun off a Vex arm? Don't bother. It won't shoot anymore.",
                  "Never trust a Scorn! They're little balls of instinct. Shoot first, talk to it later.",
                  "We'll never see eye to eye... to eye with the Hive. Go poke 'em out!" , "Hey, you fight dirty. I like it."]
        reply = random.choice(quotes)
        await ctx.send(reply)

    @commands.command()
    async def gamer(self, ctx):
        await ctx.send("im mining.")

    @commands.command()
    async def wholesome(self, ctx):
        await ctx.send("MISTER BEEEAAAST!")


    @commands.command()
    async def cayde(self, ctx):
        quotes = [
            "Ah, a night person, I get it.",
            "Alright. Get out there. Do something meaningful with your life.",
            "Alright, I'll be right here... as always.",
            "Alright, I'll be right here... *sigh* like it or not.",
            "Alright, see you around.",
            "And back into the wild with you.",
            "...and send in the cavalry.",
            "Been a long day?",
            "Can you use something here?",
            "Crota and Oryx. Racking 'em up, aren't ya?",
            "Damn, I envy you.",
            "Deep in the dead zone. Getting there will be half the fun.",
            "Eh, starting to miss the little guy...",
            "Evening.",
            "'ey, what's the story, kid?",
            "Get back out there.",
            "Get in there, kill the Taken and give yourself a pat on the back. In that order.",
            "Guardian, good luck out there.",
            "I gotta get out of this Tower and back out there.",
            "Hey, are you wasting my time?",
            "Hey, back from the wild?",
            "Hey uh, (whispers) take me with you.",
            "(whispers) Hey, take me with you?",
            "(whispers) Hey. Take me with you. I hate this job.",
            "Hey Guardian, long day?",
            "Hey, Guardian. Wake up.",
            "Hey, how about you pull up a chair? Get a drink? I'm being sarcastic.",
            "Hey, if you're not gonna buy something, how about you step aside.",
            "Hey Ikora, wanna bet a Hunter finds their mark before you?",
            "Hey, next time you anger some hideous cosmic monster, try and make it a smaller one.",
            "Hey. Stay alert out there.",
            "Hey there.",
            "Hey, you're back from the frontier?",
            "How do these look?",
            "I believe... you're looking... for this.",
            "I got what you need.",
            "I gotta get out of this tower and back out there.",
            "I need to know what happened on that moon.",
            "(sighs) I should be out there myself.",
            "I'll be out here, don't feel bad for me. Go out there and have fun, have adventures, and do something meaningful with your life.",
            "I'm starting to miss the little guy.",
            "I should have gone myself, THIS is on me.",
            "Ikora, new bet, usual terms.",
            "Keep your head down.",
            "Like anything you see?",
            "Long day, Guardian?",
            "Look, I'd love to stand here with you all day, but... *tut* I got a... a show I like to binge watch... it was... cancelled early. Still love it.",
            "Man, I wish I could have been there to see Oryx fall.",
            "Not a library. Move along.",
            "Oh, that's bad.",
            "Okay, wait, stop, go back, go back, okay.",
            "Oops, bad intel, I guess.",
            "See you around.",
            "Stay alert out there.",
            "Still have Taken to kill. I hear they're good sport.",
            "Tell me about the Dreadnaught.",
            "Tell me something interesting.",
            "Titan!"]
        reply = random.choice(quotes)
        await ctx.send(reply)


def setup(bot):
    return bot.add_cog(Hello(bot))
