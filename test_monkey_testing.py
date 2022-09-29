from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.alert import Alert
import time
import os
import random

driver = webdriver.Chrome(service=Service(r"C:\Program Files (x86)/chromedriver.exe"))  # This is a typical path for
# Windows, if there is a need to make it work on other operating systems it can be done with 'if' statements for example
p = 0.7
# That variable is created for time.sleep() functions, so I don't have to repeat myself that much on the
# following code. It's made for short waits, so user can see what is happening.
i = 5
# That variable is created for implicitly.wait() function, so I don't have to repeat myself that much on the
# following code. It's made to be sure that the following code works as it should do.
s = 2
# That variable is created for time.sleep() functions, so I don't have to repeat myself that much on the
# following code. It's made for longer waits in cases when shorter waits(p) might not be enough.


# For quite the intelligent monkey testing names are generated from the name.text file.
def load_name():
    with open("name.txt", "r") as f:
        lines = f.readlines()
        return random.choice(lines).strip()


# For quite the intelligent monkey testing last names are generated from the last_name.text file.
def load_last_name():
    with open("last_name.txt", "r") as f:
        lines = f.readlines()
        return random.choice(lines).strip()


# Dates are generated with day, month and year combined. I made the number of days in a month to be as legit as
# possible, so you shouldn't see any Easter Eggs like 30th of February.:)
def date():
    month = random.randint(1, 12)
    year = random.randint(1930, 2021)
    if month == 2 and year % 4 != 0:
        day = random.randint(1, 28)
    elif month == 2 and year % 4 == 0:
        day = random.randint(1, 29)
    elif month == 4 or 6 or 9 or 11:
        day = random.randint(1, 30)
    else:
        day = random.randint(1, 31)
    return f"{day}.{month}.{year}"


def test_setup():
    driver.get("https://www.tutorialspoint.com/selenium/selenium_automation_practice.htm")
    driver.implicitly_wait(i)
    driver.maximize_window()
    assert driver.title == 'Selenium - Automation Practice Form'


def test_form():
    driver.find_element(By.XPATH, "/html/body/div[4]/div[2]/div[1]/div[2]/div[2]/button[1]/p").click()
    driver.implicitly_wait(i)
    driver.execute_script("window.scrollBy(0,800)", "")
    time.sleep(s)
    driver.find_element(By.NAME, "firstname").send_keys(load_name())
    time.sleep(p)
    driver.find_element(By.NAME, "lastname").send_keys(load_last_name())
    time.sleep(p)
    driver.find_element(By.CSS_SELECTOR, "#mainContent > div:nth-child(9) > div > form > table > tbody > "
                                         "tr:nth-child(5) > td:nth-child(2) > input[type=text]").send_keys(date())
    time.sleep(p)
    ele = driver.find_element(By.NAME, "sex")
    driver.execute_script("arguments[0].click();", ele)
    time.sleep(p)
    driver.find_element(By.CSS_SELECTOR, "#mainContent > div:nth-child(9) > div > form > table > tbody > tr:nth-child"
                                         "(4) > td:nth-child(2) > span:nth-child(1) > input[type=radio]").click()
    time.sleep(p)
    driver.find_element(By.CSS_SELECTOR, "#mainContent > div:nth-child(9) > div > form > table > tbody >"
                                         " tr:nth-child(6) > td:nth-child(2) > span:nth-child(2) > input[typ"
                                         "e=checkbox]").click()
    time.sleep(p)
    driver.find_element(By.NAME, "photo").send_keys(os.getcwd() + "/sampleFile.jpeg")
    time.sleep(p)
    driver.find_element(By.XPATH, "//*[@id='mainContent']/div[6]/div/form/table/tbody"
                                  "/tr[8]/td[2]/span[3]/input").click()
    time.sleep(p)
    driver.find_element(By.NAME, "continents").send_keys("Antarctica")
    Select(driver.find_element(By.NAME, "selenium_commands")).select_by_visible_text("Wait Commands")
    Select(driver.find_element(By.NAME, "selenium_commands")).select_by_visible_text("Navigation Commands")
    Select(driver.find_element(By.NAME, "selenium_commands")).select_by_visible_text("WebElement Commands")
    Select(driver.find_element(By.NAME, "selenium_commands")).select_by_visible_text("Browser Commands")
    time.sleep(s)
    driver.find_element(By.NAME, "submit").click()
    driver.implicitly_wait(i)
    time.sleep(s)
    Alert(driver).accept()
    time.sleep(s)
    assert driver.title == "Selenium - Automation Practice Form"


def test_tear_down():
    driver.implicitly_wait(i)
    driver.quit()
