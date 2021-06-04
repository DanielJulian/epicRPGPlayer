from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
import queue
import _thread

class CommandWorker():

    command_queue = None
    driver = None

    def __init__(self, command_queue, driver):
      self.command_queue = command_queue
      self.driver = driver

    def send(self, driver, command):
        actions = ActionChains(driver)
        actions.send_keys(command)
        actions.send_keys(Keys.ENTER)
        actions.perform()

    def command_handler(self):
        while True:
            try:
                command = self.command_queue.get(True, 10)  # Waits for 10 seconds, otherwise throws `Queue.Empty`
            except queue.Empty:
                command = None

            if command:
                time.sleep(2)
                self.send(self.driver, command)
                time.sleep(2)

    def initialize(self):
        try:
         _thread.start_new_thread(self.command_handler, ())
        except Exception as e:
            print ("Yikes")
            print(e)