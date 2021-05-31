import discord
import winsound
import time
import _thread
from .listenerParser import getLifeRemaining

        

class DiscordListener(discord.Client):
    feedback_queue = None

    def set_feedback_queue(self, feedback_queue):
        self.feedback_queue = feedback_queue

    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        if str(message.author) == 'EPIC RPG#4117':
            if message.content.startswith("**Dano**"):
                print("-------------------------------------------------------------------------------------------")
                print("Got a message from EPIC RPG " + str(message.content))
                if 'remaining HP is' in message.content:
                    life_remaining = getLifeRemaining(message.content)
                    if life_remaining and int(life_remaining) < 40:
                        print("Sending Drink a potion message")
                        time.sleep(2)
                        self.feedback_queue.put("Drink a potion bro!")
            elif "We have to check you are actually playing" in message.content and "Dhanos" in message.content:
                duration = 500  # milliseconds
                freq = 440  # Hz
                for _ in range(0,20):
                    winsound.Beep(freq, duration)
                    winsound.Beep(freq, duration)
                    winsound.Beep(freq, duration)
                    time.sleep(1)
        elif str(message.author) == 'Dano#9151':
            print("-------------------------------------------------------------------------------------------")
            print("Dano sent a message: " + message.content)

