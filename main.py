import queue
from properties_reader import get_properties_dict
from seleniumManager.selenium_manager import SeleniumManager
from discordListener.discord_listener import DiscordListener

print("<<<<<<<Initializing EPIC RPG Automated Player>>>>>>>")

print("---------------Loading Configuration----------------")
properties = get_properties_dict()

print("-------------Creating Data Structures---------------")
feedback_queue = queue.Queue()

print("-------------Starting Selenium Manager--------------")
manager = SeleniumManager(feedback_queue)
manager.start_threads()

print("-------------Starting Discord Listener--------------")
listener = DiscordListener()
listener.set_feedback_queue(feedback_queue)
listener.run(properties['discord_bot_token'])