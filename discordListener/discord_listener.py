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
                        self.feedback_queue.put("Drink a potion bro!")
            elif "you don't have a life potion to do this" in message.content:
                print("Sending buy a potion message")
                self.feedback_queue.put("Buy some potions bro!")
            elif "We have to check you are actually playing" in message.content and "191356760873893890" in message.content: # 191356760873893890 is my ID
                # TODO Fixear esto
                # El mensaje es así:
                # :police_car: **EPIC GUARD**: stop there, <@191356760873893890>
                # We have to check you are actually playing
                print(message.content)
                #if "Dhanos" in message.content:
                duration = 500  # milliseconds
                freq = 440  # Hz
                for _ in range(0,2):
                    winsound.Beep(freq, duration)
                    winsound.Beep(freq, duration)
                    winsound.Beep(freq, duration)
                    time.sleep(1)
        
        elif "rpg arena" in message.content:
            print(str(message.author) + " created an arena... Joining")
            self.feedback_queue.put("Join Arena")
        elif "rpg miniboss" in message.content:
            print(str(message.author) + " will fight a miniboss... Fighto!!")
            self.feedback_queue.put("Join Fight")
        elif message.content.startswith("<@&848779233706770483>"): # <@&848779233706770483> is the ID for @EPICARDOS
            requested_work = message.content.replace("<@&848779233706770483>", "").strip().lower()
            print(str(message.author) + " asked everyone to " + requested_work + "!")
            if ('chop' in requested_work):
                self.feedback_queue.put("help chopin!")
            elif ('fish' in requested_work):
                self.feedback_queue.put("help fishin!")
            elif ('catch' in requested_work):
                self.feedback_queue.put("help catchin!")
            elif ('summon' in requested_work):
                self.feedback_queue.put("help sumonnin!")

        # Always log my stuff
        if str(message.author) == 'Dano#9151':
            print("-------------------------------------------------------------------------------------------")
            print("Dano sent a message: " + message.content)
        


            
