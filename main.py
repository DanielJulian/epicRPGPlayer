import queue
import os
from properties_loader import load_properties
from seleniumManager.selenium_manager import SeleniumManager
from discordListener.discord_listener import DiscordListener

print("<<<<<<<Initializing EPIC RPG Automated Player>>>>>>>")

print("---------------Loading Configuration----------------")
load_properties()

print("-------------Creating Data Structures---------------")
feedback_queue = queue.Queue()

print("-------------Starting Selenium Manager--------------")
manager = SeleniumManager(feedback_queue)
manager.start_threads()

print("-------------Starting Discord Listener--------------")
listener = DiscordListener()
listener.set_feedback_queue(feedback_queue)
listener.run(os.getenv('discord_bot_token'))