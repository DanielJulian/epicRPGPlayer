import queue
import os
from properties_loader import load_properties
from seleniumManager.selenium_manager import SeleniumManager
from discordListener.discord_listener import DiscordListener
from discordListener.discord_cache import InventoryCache

print("<<<<<<<Initializing EPIC RPG Automated Player>>>>>>>")

print("---------------Loading Configuration----------------")
load_properties()

print("-------------Creating Data Structures---------------")
feedback_queue = queue.Queue()
inventoryCache = InventoryCache()

print("-------------Starting Selenium Manager--------------")
manager = SeleniumManager(feedback_queue, inventoryCache)

print("-------------Starting Discord Listener--------------")
listener = DiscordListener()
listener.set_feedback_queue(feedback_queue)
listener.set_inventory_cache(inventoryCache)
listener.run(os.getenv('discord_bot_token'))


# TODOs

# Si me aparece la poli, de alguna manera bloquear el CommandWorker hasta que lo haya resuelto.

# Hacer que el command worker tome una lista d ecomandos para ejecutar secuencialmente.
# Hacer que el bot acepte duelos y elije una de las 3 opciones solo
