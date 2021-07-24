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

   threads_already_running = False
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
      _thread.start_new_thread(self.feedback_handler, ())

   def initialize_selenium_manager(self):
      self.driver = webdriver.Chrome()
      self.driver.get("https://discord.com/channels/532406798569963523/848456201040691211") # EPIC RPG Channel
      login(self.driver)
      time.sleep(5)

   def work(self, initial_cooldown=0):
      time.sleep(initial_cooldown)
      working_commands = ast.literal_eval(os.getenv('work_commands')) # 'Chop', 'Fish', 'Mine', 'Axe', 'Net', 'Pickup'
      while True:
         self.command_queue.put("rpg " + random.choice(working_commands))
         time.sleep(302 + randint(0, 10)) # 5 min 2 secs + random 

   def hunt(self, initial_cooldown=0):
      time.sleep(initial_cooldown)
      while True:
         self.command_queue.put('rpg hunt')
         time.sleep(61 + randint(0, 10)) # 61 secs + random
   
   def weekly(self, initial_cooldown=0):
      time.sleep(initial_cooldown)
      while True:
         self.command_queue.put('rpg weekly')
         time.sleep(604800) # 1 Week
   
   def daily(self, initial_cooldown=0):
      time.sleep(initial_cooldown)
      while True:
         self.command_queue.put('rpg daily')
         time.sleep(86500) # 24 Hours
   
   def lootbox(self, initial_cooldown=0):
      time.sleep(initial_cooldown)
      while True:
         self.command_queue.put('rpg withdraw 500k')
         self.command_queue.put('rpg buy edgy lootbox')
         self.command_queue.put('rpg deposit all')
         time.sleep(10900) # 3 Hours

   def farm(self, initial_cooldown=0):
      time.sleep(initial_cooldown)
      
      def get_seeds_in_inventory():
         seed_list = []
         for item_name, amount in self.inventory_cache.get_consumables().items():
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

   def adventure(self, initial_cooldown=0):
      time.sleep(initial_cooldown)
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
            if type(feedback_message) is dict:
               self.start_threads(feedback_message)
            elif feedback_message == 'Drink a potion bro!':
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
               self.farm(0)
            elif feedback_message == "Check Cooldowns":
               self.command_queue.put('rpg cd')
               
     
               
   def start_threads(self, initial_cds):
      if (self.threads_already_running == False):
         try:
            time.sleep(1)
            if (os.getenv('work.enabled', 'False') == 'True'):
               _thread.start_new_thread(self.work, (initial_cds['work_cd_secs'],))
               time.sleep(1)
            if (os.getenv('hunt.enabled', 'False') == 'True'):
               _thread.start_new_thread(self.hunt, (initial_cds['hunt_cd_secs'],))
               time.sleep(1)
            if (os.getenv('farm.enabled', 'False') == 'True'):
               _thread.start_new_thread(self.farm, (initial_cds['farm_cd_secs'],))
               time.sleep(1)
            if (os.getenv('weekly.enabled', 'False') == 'True'):
               _thread.start_new_thread(self.weekly, (initial_cds['weekly_cd_secs'],))
               time.sleep(1)
            if (os.getenv('daily.enabled', 'False') == 'True'):
               _thread.start_new_thread(self.daily, (initial_cds['daily_cd_secs'],))
               time.sleep(1)
            if (os.getenv('lootbox.enabled', 'False') == 'True'):
               _thread.start_new_thread(self.lootbox, (initial_cds['lootbox_cd_secs'],))
               time.sleep(1)
            if (os.getenv('adventure.enabled', 'False') == 'True'):
               _thread.start_new_thread(self.adventure, (initial_cds['adventure_cd_secs'],))
            self.threads_already_running = True
         except Exception as e:
            print ("Yikes")
            print(e)


   def close_driver(self):
      driver.close()
