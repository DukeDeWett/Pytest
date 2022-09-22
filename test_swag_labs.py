from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(service=Service(r"C:\Program Files (x86)/chromedriver.exe"))


def test_setup():
    driver.get("https://www.saucedemo.com/")
    driver.implicitly_wait(10)
    driver.maximize_window()


# Firstable I have sent keys for profile that is destined to fail, so then I could try to log into standard account
# which works correctly.
def test_login():
    driver.implicitly_wait(2)
    driver.find_element(By.ID, "user-name").send_keys("locked_out_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    time.sleep(2)
    log = driver.find_element(By.ID, "user-name")
    log.send_keys(Keys.CONTROL, 'a')
    log.send_keys(Keys.BACKSPACE)
    log.send_keys("standard_user")
    driver.find_element(By.ID, "login-button").click()


# Here I wanted to check how works the buying process and also what happens if you decide remove one of those items from
# the cart.
def test_purchase():
    driver.implicitly_wait(5)
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    time.sleep(2)
    driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()
    driver.find_element(By.ID, "add-to-cart-test.allthethings()-t-shirt-(red)").click()
    time.sleep(2)
    driver.find_element(By.ID, "remove-sauce-labs-backpack").click()
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR, "#shopping_cart_container > a").click()
    time.sleep(1)


# This is a simple checkout procedure without any turbulences.
def test_checkout():
    time.sleep(2)
    driver.find_element(By.ID, "checkout").click()
    driver.implicitly_wait(5)
    driver.find_element(By.ID, "first-name").send_keys("Standard")
    driver.find_element(By.ID, "last-name").send_keys("User")
    driver.find_element(By.ID, "postal-code").send_keys("44222")
    time.sleep(2)
    driver.find_element(By.ID, "continue").click()
    time.sleep(2)


def test_closure():
    driver.implicitly_wait(5)
    driver.find_element(By.ID, "finish").click()
    time.sleep(2)


def test_teardown():
    driver.quit()
    print("Test completed")
