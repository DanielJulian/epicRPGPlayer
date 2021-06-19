import sys
import os
import discord
import winsound
import time
import _thread
from .listenerParser import getLifeRemaining


class DiscordListener(discord.Client):
    
    feedback_queue = None
    inventory_cache = None

    def set_feedback_queue(self, feedback_queue):
        self.feedback_queue = feedback_queue
    
    def set_inventory_cache(self, inventory_cache):
        self.inventory_cache = inventory_cache

    def windows_beep(self, duration, frequency):
        for _ in range(0,2):
            winsound.Beep(frequency, duration)
            winsound.Beep(frequency, duration)
            winsound.Beep(frequency, duration)
            time.sleep(1)
    
    def check_if_im_in_jail(self, message):
        if any(name in message.content.lower() for name in [os.getenv('discord_user_id').lower(), os.getenv('discord_user_name').lower()]): # EPIC RPG Message was sent to me 
            if ("you are in the" in message.content.lower() and "jail" in message.content.lower()) or ("is now in the jail" in message.content):
                print("We are in Jail... lets stop the bot.")
                self.windows_beep(300, 2000)
                self.windows_beep(300, 2000)
                sys.exit()

    def handle_epicardos_tag(self, message):
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

    def check_embeds(self, embeds):
        for embed in embeds: # Check for embeds
            embed_dict = embed.to_dict()
            if ('author' in embed_dict):
                if (embed_dict['author']['name'].lower() == os.getenv('discord_user_name').lower() + "'s inventory"): # Looking at my inventory
                    for field in embed_dict['fields']:
                        self.inventory_cache.update_inventory(field)

    def handle_epic_rpg_message(self, message):
        self.check_embeds(message.embeds)
        self.check_if_im_in_jail(message)
        
        print("X- " + message.content)
        # EPIC RPG Message was sent to me 
        if any(name in message.content.lower() for name in [os.getenv('discord_user_id').lower(), os.getenv('discord_user_name').lower()]):
            if 'remaining HP is' in message.content:
                life_remaining = getLifeRemaining(message.content)
                if life_remaining and int(life_remaining) <= int(os.getenv('hp_threshold')):
                    print("Sending Drink a potion message")
                    self.feedback_queue.put("Drink a potion bro!")

            elif "you don't have a life potion to do this" in message.content:
                print("Sending buy a potion message")
                self.feedback_queue.put("Buy some potions bro!")

            elif "We have to check you are actually playing" in message.content:
                self.windows_beep(500, 400)
            
            elif "you need a" in message.content and "seed to farm" in message.content: # Out of seeds
                print("Out of seeds, sending message to buy...")
                self.feedback_queue.put("Buy seed")

    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        if str(message.author) == 'EPIC RPG#4117':
            self.handle_epic_rpg_message(message)
        
        elif "rpg arena" in message.content.strip().lower():
            print(str(message.author) + " created an arena... Joining")
            self.feedback_queue.put("Join Arena")

        elif "rpg miniboss" in message.content.strip().lower():
            print(str(message.author) + " will fight a miniboss... Lets fight!!")
            self.feedback_queue.put("Join Fight")

        elif message.content.startswith("<@&848779233706770483>"): # <@&848779233706770483> is the ID for @EPICARDOS
            self.handle_epicardos_tag(message)

        # Always log my stuff
        if str(message.author) == os.getenv('discord_user_name_and_tag'):
            print("-------------------------------------------------------------------------------------------")
            print(os.getenv('discord_user_name') + " sent a message: " + message.content)
        

