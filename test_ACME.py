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
def test_setup():
    driver.implicitly_wait(10)
    driver.maximize_window()
    yield
    driver.close()
    driver.quit()
    print("Test completed")


def test_login():
    driver.get("http://a.testaddressbook.com/")
    driver.implicitly_wait(4)
    driver.maximize_window()
    log = driver.find_element(By.ID, "sign-in")
    log.click()
    driver.implicitly_wait(5)
    log = driver.find_element(By.NAME, "session[email]")
    log.send_keys("wowow@uwu.ss")
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
    address = driver.find_element(By.XPATH, "/html/body/nav/div/div[1]/a[2]")
    address.click()
    driver.implicitly_wait(4)
    address = driver.find_element(By.LINK_TEXT, "New Address")
    address.click()
    driver.implicitly_wait(3)
    address = driver.find_element(By.ID, "address_first_name")
    address.send_keys("Don")
    address = driver.find_element(By.ID, "address_last_name")
    address.send_keys("Kichot")
    address = driver.find_element(By.ID, "address_street_address")
    address.send_keys("La")
    address = driver.find_element(By.ID, "address_secondary_address")
    address.send_keys("Mancha")
    address = driver.find_element(By.ID, "address_city")
    address.send_keys("Windmill")
    address = driver.find_element(
        By.XPATH, "/html/body/div/div/div/form/div[6]/select/option[8]")
    address.click()
    address = driver.find_element(By.ID, "address_zip_code")
    address.send_keys("44222")
    address = driver.find_element(By.ID, "address_country_us")
    address.click()
    address = driver.find_element(By.ID, "address_birthday")
    address.click()
    address.send_keys(Keys.ARROW_LEFT, Keys.ARROW_LEFT)
    address.send_keys("12052001")
    address = driver.find_element(By.ID, "address_age")
    address.send_keys("18")
    address = driver.find_element(By.ID, "address_website")
    address.send_keys("http://www.notsohasty.com")
    address = driver.find_element(By.ID, "address_phone")
    address.send_keys("555333111")
    address = driver.find_element(By.XPATH, "/html/body/div/div/div/form/div[15]/input[2]")
    address.click()
    address = driver.find_element(By.ID, "address_note")
    address.send_keys("Thanks for this wholesome journey")
    address = driver.find_element(By.ID, "address_color")
    address.send_keys('#FF0000')
    address = driver.find_element(By.XPATH, "/html/body/div/div/div/form/div[17]/input")
    address.click()
    time.sleep(2)
    driver.quit()
