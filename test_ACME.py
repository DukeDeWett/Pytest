from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os


driver = webdriver.Chrome(service=Service(r"C:\Program Files (x86)/chromedriver.exe"))
p = 0.7
# That variable is created for time.sleep() functions, so I don't have to repeat myself that much on the
# following code.
i = 5
# That variable is created for implicitly.wait() function, so I don't have to repeat myself that much on the
# following code.


def test_setup():
    driver.get("http://a.testaddressbook.com/")
    driver.implicitly_wait(i)
    driver.maximize_window()
    assert not isinstance(driver, type(webdriver))
    print(driver.title)
    assert driver.title == 'Address Book'


def test_login():
    driver.implicitly_wait(i)
    driver.find_element(By.ID, "sign-in").click()
    driver.implicitly_wait(i)
    driver.find_element(By.NAME, "session[email]").send_keys("wowow@uwu.ss")
    log = driver.find_element(By.NAME, "session[password]")
    log.send_keys("ddjcdjcd")
    log.send_keys(Keys.ENTER)
    driver.implicitly_wait(i)
    assert driver.title == 'Address Book'


def test_addresses():
    driver.find_element(By.XPATH, "/html/body/nav/div/div[1]/a[2]").click()
    driver.implicitly_wait(i)
    driver.find_element(By.LINK_TEXT, "New Address").click()
    time.sleep(p)
    driver.implicitly_wait(3)
    driver.find_element(By.ID, "address_first_name").send_keys("Don")
    time.sleep(p)
    driver.find_element(By.ID, "address_last_name").send_keys("Kichot")
    time.sleep(p)
    driver.find_element(By.ID, "address_street_address").send_keys("La")
    time.sleep(p)
    driver.find_element(By.ID, "address_secondary_address").send_keys("Mancha")
    time.sleep(p)
    driver.find_element(By.ID, "address_city").send_keys("Windmill")
    time.sleep(p)
    driver.find_element(
        By.XPATH, "/html/body/div/div/div/form/div[6]/select/option[8]").click()
    time.sleep(p)
    driver.find_element(By.ID, "address_zip_code").send_keys("44222")
    time.sleep(p)
    driver.find_element(By.ID, "address_country_us").click()
    time.sleep(p)
    address = driver.find_element(By.ID, "address_birthday")
    address.click()
    address.send_keys(Keys.ARROW_LEFT, Keys.ARROW_LEFT)
    address.send_keys("12052001")
    time.sleep(p)
    driver.find_element(By.ID, "address_age").send_keys("18")
    time.sleep(p)
    driver.find_element(By.ID, "address_website").send_keys("http://www.notsohasty.com")
    time.sleep(p)
    driver.implicitly_wait(i)
    driver.find_element(By.ID, "address_picture").send_keys(os.getcwd() + "/sampleFile.jpeg")
    time.sleep(p)
    driver.find_element(By.ID, "address_phone").send_keys("555333111")
    time.sleep(p)
    driver.find_element(By.XPATH, "/html/body/div/div/div/form/div[15]/input[2]").click()
    time.sleep(p)
    driver.find_element(By.ID, "address_note").send_keys("Thanks for this wholesome journey")
    time.sleep(p)
    driver.find_element(By.ID, "address_color").send_keys('#FF0000')
    time.sleep(p)
    assert driver.title == 'Address Book'


def test_tear_down():
    driver.find_element(By.XPATH, "/html/body/div/div/div/form/div[17]/input").click()
    time.sleep(3)
    driver.implicitly_wait(i)
    print("All tests completed!")
    driver.quit()
