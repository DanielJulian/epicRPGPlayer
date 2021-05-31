import queue
from seleniumManager.selenium_manager import SeleniumManager
from discordListener.discord_listener import DiscordListener

print("<<<<<<<Initializing EPIC RPG Automated Player>>>>>>>")

print("-------------Creating Data Structures---------------")
feedback_queue = queue.Queue()

print("-------------Starting Selenium Manager--------------")
manager = SeleniumManager(feedback_queue)
manager.start_threads()


print("-------------Starting Discord Listener--------------")
listener = DiscordListener()
listener.set_feedback_queue(feedback_queue)
tk1="ODQ4NzI5NDI3MjkzODk2NzA0"  
tk2=".YLQ24A.mfml3tOd9CKbXLPL72CLA2vPBlo"
listener.run(tk1+tk2)