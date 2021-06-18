import os
import time
import _thread
import ast
import queue
import random
from random import randint
from .utils.discord_login import login
from .command_worker import CommandWorker
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class SeleniumManager():

   inventory_cache = None
   command_queue = None
   feedback_queue = None
   driver = None

   def __init__(self, feedback_queue, inventory_cache):
      self.feedback_queue = feedback_queue
      self.inventory_cache = inventory_cache
      self.initialize_selenium_manager()
      self.command_queue = queue.Queue()
      print("Initializing Command Worker")
      command_worker = CommandWorker(self.command_queue, self.driver)
      command_worker.initialize()

   def initialize_selenium_manager(self):
      self.driver = webdriver.Chrome()
      self.driver.get("https://discord.com/channels/532406798569963523/848456201040691211") # EPIC RPG Channel
      login(self.driver)
      time.sleep(5)

   def work(self):
      working_commands = ast.literal_eval(os.getenv('work_commands')) # 'Chop', 'Fish', 'Mine', 'Axe', 'Net', 'Pickup'
      while True:
         self.command_queue.put("rpg " + random.choice(working_commands))
         time.sleep(302 + randint(0, 10)) # 5 min 2 secs + random 

   def hunt(self):
      while True:
         self.command_queue.put('rpg hunt')
         time.sleep(61 + randint(0, 10)) # 61 secs + random

   def farm(self):
      
      def get_seeds_in_inventory():
         seed_list = []
         for item_name, amount in self.inventory_cache.get_consumables().items():
            print(item_name, amount)
            if 'seed' in item_name and amount > 0 and item_name != 'seed':
               seed_list.append(item_name)
         return seed_list

      while True:
         self.command_queue.put("rpg i") # To refresh inventory cache
         time.sleep(10)
         command = 'rpg farm'
         seed_list = get_seeds_in_inventory()
         if (seed_list): 
            command += " " + random.choice(seed_list)
         self.command_queue.put(command)
         time.sleep(610 + randint(0, 10)) # 10 minutes 10 secs + random

   def adventure(self):
      while True:
         self.command_queue.put('rpg heal')
         self.command_queue.put('rpg adventure')
         time.sleep(3601 + randint(0, 10)) # 1 hour + random secs

   def feedback_handler(self):
      while True:
         try:
            feedback_message = self.feedback_queue.get(True, 10)  # Waits for 10 seconds, otherwise throws `Queue.Empty`
         except queue.Empty:
            feedback_message = None
            
         if feedback_message:
            if feedback_message == 'Drink a potion bro!':
               self.command_queue.put('rpg heal')
            elif feedback_message == 'Buy some potions bro!':
               self.command_queue.put('rpg buy life potion 30')
            elif feedback_message == 'Join Arena':
               self.command_queue.put('join')
            elif feedback_message == 'Join Fight':
               self.command_queue.put('fight')
            elif feedback_message == 'help chopin!':
               self.command_queue.put('chop')
            elif feedback_message == 'help fishin!':
               self.command_queue.put('fish')
            elif feedback_message == 'help catchin!':
               self.command_queue.put('catch')
            elif feedback_message == 'help sumonnin!':
               self.command_queue.put('summon')
            elif feedback_message == "Buy seed":
               self.command_queue.put('rpg buy seed')
               self.farm()
               

               
   def start_threads(self):
      try:
         _thread.start_new_thread(self.feedback_handler, ())
         time.sleep(1)
         _thread.start_new_thread(self.work, ())
         time.sleep(1)
         _thread.start_new_thread(self.hunt, ())
         time.sleep(1)
         _thread.start_new_thread(self.farm, ())
         time.sleep(1)
         _thread.start_new_thread(self.adventure, ())
      except Exception as e:
         print ("Yikes")
         print(e)


   def close_driver(self):
      driver.close()

