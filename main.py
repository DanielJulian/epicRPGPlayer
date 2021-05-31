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
listener = DiscordListener(feedback_queue).Listener()
listener.run('ODQ4NzI5NDI3MjkzODk2NzA0.YLQ24A.S8xEpT0O3b3FLxWm2rkxajbDT9Q')