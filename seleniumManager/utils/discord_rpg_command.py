from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

prefix = "rpg "

def send(driver, command):
    actions = ActionChains(driver)
    actions.send_keys(prefix + command)
    actions.send_keys(Keys.ENTER)
    actions.perform()
    