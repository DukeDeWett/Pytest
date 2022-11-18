import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from page_objects_UQ.header import Header
from page_objects_UQ.body import Body
from page_objects_UQ.footer import Footer
import logging


@pytest.fixture()
def driver():
    driver = webdriver.Chrome(service=Service(r"C:\Program Files (x86)/chromedriver.exe"))
    driver.maximize_window()
    yield driver
    driver.quit()


def go_back(driver):
    driver.implicitly_wait(5)
    driver.back()


def wait(driver):
    driver.implicitly_wait(5)


# For each button or link I had to use specific selector that is why it is very diverse, even when it does not need
# to be.
def test_easy(driver):
    driver.get("https://ultimateqa.com/simple-html-elements-for-automation/")
    wait(driver)
    driver.find_element(*Header.BUTTON1).click()
    go_back(driver)
    driver.find_element(*Header.BUTTON2).click()
    go_back(driver)
    wait(driver)
    driver.find_element(*Header.BUTTON3).click()
    go_back(driver)
    driver.find_element(*Header.LINK1).click()
    go_back(driver)
    driver.find_element(*Header.BUTTON4).click()
    go_back(driver)
    driver.find_element(*Header.BUTTON5).click()
    go_back(driver)
    wait(driver)
    logging.info("Phase one - passed")


# This one is more interesting. Except clicking into different links or buttons it's also sends some
# form and validates the options that were or were not chosen.
def test_mid(driver):
    # this selector is huge, but that was the only way to make it work with selenium
    driver.get("https://ultimateqa.com/simple-html-elements-for-automation/")
    wait(driver)
    driver.find_element(*Body.BUTTON1).click()
    go_back(driver)
    driver.find_element(*Body.LINK1).click()
    go_back(driver)
    driver.find_element(*Body.ICON1).click()
    go_back(driver)
    driver.find_element(*Body.ICON2).click()
    go_back(driver)
    driver.find_element(*Body.NAME).send_keys(*Body.KEY1)
    driver.find_element(*Body.MAIL).send_keys(*Body.KEY2)
    wait(driver)
    driver.find_element(*Body.BUTTON2).click()
    wait(driver)
    driver.find_element(*Body.RADIO1).click()
    wait(driver)
    medium = driver.find_element(*Body.CHECKBOX)
    medium.click()
    wait(driver)
    logging.info(r"Is 'other' selected?")
    logging.info(medium.is_selected())
    medium = driver.find_element(*Body.CHECKBOX2)
    wait(driver)
    medium.click()
    logging.info("Is bike option selected?")
    logging.info(medium.is_selected())
    medium = driver.find_element(*Body.DROPDOWN)
    medium.send_keys(*Body.CAR)
    wait(driver)
    logging.info("Is car option selected?")
    logging.info(medium.is_selected())
    logging.info("Is Saab selected?")
    logging.info(medium.is_selected())
    medium = driver.find_element(*Body.TAB)
    wait(driver)
    medium.click()
    logging.info("Is tab 1 selected?")
    logging.info(medium.is_selected())
    logging.info("Phase two - passed")
    wait(driver)


# That is the last part. I was supposed to find elements via XPATH, and then I had to highlight the "HIGHLIGHT ME"
# texts, and I thought that instead of click and drag it I want them to be highlighted separately.
def test_down(driver):
    driver.get("https://ultimateqa.com/simple-html-elements-for-automation/")
    wait(driver)
    driver.find_element(*Footer.BUTTON1).click()
    go_back(driver)
    driver.find_element(*Footer.BUTTON2).click()
    go_back(driver)
    driver.find_element(*Footer.BUTTON3).click()
    go_back(driver)
    driver.find_element(*Footer.BUTTON4).click()
    go_back(driver)
    medium = driver.find_element(*Footer.HIGHLIGHT1)
    wait(driver)
    action = ActionChains(driver)
    action.double_click(medium).click().perform()
    medium = driver.find_element(*Footer.HIGHLIGHT2)
    wait(driver)
    action = ActionChains(driver)
    action.double_click(medium).click().perform()
    medium = driver.find_element(*Footer.HIGHLIGHT3)
    wait(driver)
    action = ActionChains(driver)
    action.double_click(medium).click().perform()
    logging.info("Last phase - passed")
