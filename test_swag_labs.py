from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pytest

driver = webdriver.Chrome(service=Service(r"C:\Program Files (x86)/chromedriver.exe"))


# For some reason this doesn't work, but without this "pytest" tests don't work, so I need to import it in some way.
# To solve this I have put its functionality in first and last tests
@pytest.fixture()
def setup_module():
    driver.implicitly_wait(10)
    driver.maximize_window()
    yield
    driver.close()
    driver.quit()
    print("Test completed")


# Firstable I have sent keys for profile that is destined to fail, so then I could try to log into standard account
# which works correctly.
def test_login():
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()
    log = driver.find_element(By.ID, "user-name")
    log.send_keys("locked_out_user")
    log = driver.find_element(By.ID, "password")
    log.send_keys("secret_sauce")
    log = driver.find_element(By.ID, "login-button")
    log.click()
    time.sleep(2)
    log = driver.find_element(By.ID, "user-name")
    log.send_keys(Keys.CONTROL, 'a')
    log.send_keys(Keys.BACKSPACE)
    log.send_keys("standard_user")
    log = driver.find_element(By.ID, "login-button")
    log.click()


# Here I wanted to check how works the buying process and also what happens if you decide remove one of those items from
# the cart.
def test_purchase():
    time.sleep(2)
    buy = driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack")
    buy.click()
    time.sleep(2)
    buy = driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie")
    buy.click()
    buy = driver.find_element(By.ID, "add-to-cart-test.allthethings()-t-shirt-(red)")
    buy.click()
    time.sleep(2)
    buy = driver.find_element(By.ID, "remove-sauce-labs-backpack")
    buy.click()
    time.sleep(3)
    buy = driver.find_element(By.CSS_SELECTOR, "#shopping_cart_container > a")
    buy.click()


# This is a simple checkout procedure without any turbulences.
def test_checkout():
    time.sleep(2)
    finish = driver.find_element(By.ID, "checkout")
    finish.click()
    driver.implicitly_wait(5)
    finish = driver.find_element(By.ID, "first-name")
    finish.send_keys("Standard")
    finish = driver.find_element(By.ID, "last-name")
    finish.send_keys("User")
    finish = driver.find_element(By.ID, "postal-code")
    finish.send_keys("44222")
    time.sleep(3)
    finish = driver.find_element(By.ID, "continue")
    finish.click()


def test_closure():
    driver.implicitly_wait(5)
    finish = driver.find_element(By.ID, "finish")
    finish.click()
    time.sleep(2)
    driver.quit()
