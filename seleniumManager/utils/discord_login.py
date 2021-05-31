from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def login(driver):
    email_element = driver.find_element_by_name("email")
    email_element.clear()
    email_element.send_keys("dani_77@live.com.ar")

    password_element = driver.find_element_by_name("password")
    password_element.clear()
    password_element.send_keys('Please123!"#')
    password_element.send_keys(Keys.RETURN)
