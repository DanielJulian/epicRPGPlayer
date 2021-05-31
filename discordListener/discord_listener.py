import discord
import winsound
import time
import _thread
from .listenerParser import getLifeRemaining

class DiscordListener():
    
    feedback_queue = None

    def __init__(self, feedback_queue):
        self.feedback_queue = feedback_queue

    class Listener(discord.Client):
        async def on_ready(self):
            print('Logged on as {0}!'.format(self.user))

        async def on_message(self, message):
            if str(message.author) == 'EPIC RPG#4117':
                if message.content.startswith("**Dano**"):
                    print("-------------------------------------------------------------------------------------------")
                    print("Got a message from EPIC RPG " + str(message))
                    if 'remaining HP is' in message.content.contains:
                        lifeRemaining = getLifeRemaining(message.content)
                        if lifeRemaining and int(lifeRemaining) < 40:
                            feedback_queue.put("Drink a potion bro!")
                elif "We have to check you are actually playing" in message.content:
                    duration = 500  # milliseconds
                    freq = 440  # Hz
                    for _ in range(0,20):
                        winsound.Beep(freq, duration)
                        winsound.Beep(freq, duration)
                        winsound.Beep(freq, duration)
                        time.sleep(1)
            elif str(message.author) == 'Dano#9151':
                print("-------------------------------------------------------------------------------------------")
                print(message)

