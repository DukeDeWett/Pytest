from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pytest

driver = webdriver.Chrome(service=Service(r"C:\Program Files (x86)/chromedriver.exe"))


# For some reason this doesn't work, but without this "pytest" tests don't work, so I need to import it in some way.
# To solve this I have put its functionality in first and last tests

def test_setup():
    driver.get("http://a.testaddressbook.com/")
    driver.implicitly_wait(10)
    driver.maximize_window()


def test_login():
    driver.implicitly_wait(1)
    driver.find_element(By.ID, "sign-in").click()
    driver.implicitly_wait(5)
    driver.find_element(By.NAME, "session[email]").send_keys("wowow@uwu.ss")
    log = driver.find_element(By.NAME, "session[password]")
    log.send_keys("ddjcdjcd")
    log.send_keys(Keys.ENTER)
    driver.implicitly_wait(5)

    # log = driver.find_element(By.LINK_TEXT, "Sign up")
    # log.click()
    # driver.implicitly_wait(5)
    # log = driver.find_element(By.NAME, "user[email]")
    # log.send_keys("wowow@uwu.ss")
    # log = driver.find_element(By.NAME, "user[password]")
    # log.send_keys("ddjcdjcd")
    # log.send_keys(Keys.ENTER)


def test_addresses():
    driver.find_element(By.XPATH, "/html/body/nav/div/div[1]/a[2]").click()
    driver.implicitly_wait(4)
    driver.find_element(By.LINK_TEXT, "New Address").click()
    driver.implicitly_wait(3)
    driver.find_element(By.ID, "address_first_name").send_keys("Don")
    driver.find_element(By.ID, "address_last_name").send_keys("Kichot")
    driver.find_element(By.ID, "address_street_address").send_keys("La")
    driver.find_element(By.ID, "address_secondary_address").send_keys("Mancha")
    driver.find_element(By.ID, "address_city").send_keys("Windmill")
    driver.find_element(
        By.XPATH, "/html/body/div/div/div/form/div[6]/select/option[8]").click()
    driver.find_element(By.ID, "address_zip_code").send_keys("44222")
    driver.find_element(By.ID, "address_country_us").click()
    address = driver.find_element(By.ID, "address_birthday")
    address.click()
    address.send_keys(Keys.ARROW_LEFT, Keys.ARROW_LEFT)
    address.send_keys("12052001")
    driver.find_element(By.ID, "address_age").send_keys("18")
    driver.find_element(By.ID, "address_website").send_keys("http://www.notsohasty.com")
    driver.find_element(By.ID, "address_phone").send_keys("555333111")
    driver.find_element(By.XPATH, "/html/body/div/div/div/form/div[15]/input[2]").click()
    driver.find_element(By.ID, "address_note").send_keys("Thanks for this wholesome journey")
    driver.find_element(By.ID, "address_color").send_keys('#FF0000')
    driver.find_element(By.XPATH, "/html/body/div/div/div/form/div[17]/input").click()
    time.sleep(3)
    print("All tests completed!")


def test_tear_down():
    driver.quit()
