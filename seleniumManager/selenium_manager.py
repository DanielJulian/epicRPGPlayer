import time
import _thread
import queue
import random
from random import randint
from .utils.discord_login import login
from .command_worker import CommandWorker
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class SeleniumManager():

   command_queue = None
   feedback_queue = None
   driver = None

   def __init__(self, feedback_queue):
      self.feedback_queue = feedback_queue
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

   def collect(self):
      activities = ['Chop', 'Fish'] # 'Pickup', 'Mine'
      while True:
         self.command_queue.put("rpg " + random.choice(activities))
         time.sleep(302 + randint(0, 10)) # 5 min 2 secs + random 

   def hunt(self):
      while True:
         self.command_queue.put('rpg hunt')
         time.sleep(61 + randint(0, 10)) # 61 secs + random

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

               
   def start_threads(self):
      try:
         _thread.start_new_thread(self.feedback_handler, ())
         _thread.start_new_thread(self.collect, ())
         _thread.start_new_thread(self.hunt, ())
         _thread.start_new_thread(self.adventure, ())
      except Exception as e:
         print ("Yikes")
         print(e)


   def close_driver(self):
      driver.close()

