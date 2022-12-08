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


def test_easy(driver):
    """For each button or link I had to use specific selector that is why it is very diverse, even when it does not need
    to be."""
    driver.get("https://ultimateqa.com/simple-html-elements-for-automation/")
    Header.BUTTON_CLICK_ME.find_me(driver).click()
    logging.info("Phase one - passed")


# def test_mid(driver):
#     """ This one is more interesting. Except clicking into different links or buttons it's also sends some
#     form and validates the options that were or were not chosen."""
#     driver.get("https://ultimateqa.com/simple-html-elements-for-automation/")
#     """ This selector is huge, but that was the only way to make it work with selenium """
#     wait(driver)
#     driver.find_element(*Body.BUTTON_SIMPLE_CONTROLS).click()
#     go_back(driver)
#     driver.find_element(*Body.CLICK_THIS_LINK).click()
#     go_back(driver)
#     driver.find_element(*Body.ICON_CLICKABLE_TEXT).click()
#     go_back(driver)
#     driver.find_element(*Body.ICON_CLICKABLE_ARROW).click()
#     go_back(driver)
#     driver.find_element(*Body.NAME).send_keys("Hello")
#     driver.find_element(*Body.MAIL).send_keys("bb@cya.bye")
#     wait(driver)
#     driver.find_element(*Body.BUTTON_EMAIL_ME).click()
#     wait(driver)
#     driver.find_element(*Body.RADIO_BUTTON).click()
#     wait(driver)
#     medium = driver.find_element(*Body.CHECKBOX)
#     medium.click()
#     wait(driver)
#     logging.info(r"Is 'other' selected?")
#     logging.info(medium.is_selected())
#     medium = driver.find_element(*Body.CHECKBOX_BUTTON)
#     wait(driver)
#     medium.click()
#     logging.info("Is bike option selected?")
#     logging.info(medium.is_selected())
#     medium = driver.find_element(*Body.DROPDOWN_MENU)
#     medium.send_keys("Saab")
#     wait(driver)
#     logging.info("Is car option selected?")
#     logging.info(medium.is_selected())
#     logging.info("Is Saab selected?")
#     logging.info(medium.is_selected())
#     medium = driver.find_element(*Body.TAB_OPTION)
#     wait(driver)
#     medium.click()
#     logging.info("Is tab 1 selected?")
#     logging.info(medium.is_selected())
#     logging.info("Phase two - passed")
#     wait(driver)
#
#
# def test_down(driver):
#     """ That is the last part. I was supposed to find elements via XPATH, and then I had to highlight the "HIGHLIGHT ME"
#     texts, and I thought that instead of click and drag it I want them to be highlighted separately."""
#     driver.get("https://ultimateqa.com/simple-html-elements-for-automation/")
#     wait(driver)
#     driver.find_element(*Footer.BUTTON_TOP_ON_GREY).click()
#     go_back(driver)
#     driver.find_element(*Footer.BUTTON_SECOND_ON_GREY).click()
#     go_back(driver)
#     driver.find_element(*Footer.BUTTON_THIRD_ON_GREY).click()
#     go_back(driver)
#     driver.find_element(*Footer.BUTTON_LAST_ON_GREY).click()
#     go_back(driver)
#     medium = driver.find_element(*Footer.HIGHLIGHT_ME_LEFT)
#     wait(driver)
#     action = ActionChains(driver)
#     action.double_click(medium).click().perform()
#     medium = driver.find_element(*Footer.HIGHLIGHT_ME_MIDDLE)
#     wait(driver)
#     action = ActionChains(driver)
#     action.double_click(medium).click().perform()
#     medium = driver.find_element(*Footer.HIGHLIGHT_ME_RIGHT)
#     wait(driver)
#     action = ActionChains(driver)
#     action.double_click(medium).click().perform()
#     logging.info("Last phase - passed")
