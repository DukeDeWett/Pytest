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


def test_easy(driver):
    driver.get("https://ultimateqa.com/simple-html-elements-for-automation/")
    Header.BUTTON_CLICK_ME.find_me(driver).click()
    driver.back()
    Header.BUTTON_RAISE.find_me(driver).click()
    driver.back()
    Header.BUTTON_GREEN_ID.find_me(driver).click()
    driver.back()
    Header.LINK_ON_BLUE.find_me(driver).click()
    driver.back()
    Header.BUTTON_CLASS_NAME_ON_BLUE.find_me(driver).click()
    driver.back()
    Header.BUTTON_NAME_ON_BLUE.find_me(driver).click()
    driver.back()
    logging.info("Phase one - passed")
    button_to_assert = Header.BUTTON_CLICK_ME.find_me(driver)
    assert button_to_assert.text == "Click Me!"


def test_mid(driver):
    driver.get("https://ultimateqa.com/simple-html-elements-for-automation/")
    """ This selector is huge, but that was the only way to make it work with selenium """
    Body.BUTTON_SIMPLE_CONTROLS.find_me(driver).click()
    driver.back()
    Body.CLICK_THIS_LINK.find_me(driver).click()
    driver.back()
    Body.ICON_CLICKABLE_TEXT.find_me(driver).click()
    driver.back()
    Body.ICON_CLICKABLE_ARROW.find_me(driver).click()
    driver.back()
    Body.NAME.find_me(driver).send_keys("Hello")
    Body.MAIL.find_me(driver).send_keys("bb@cya.bye")
    Body.BUTTON_EMAIL_ME.find_me(driver).click()
    Body.RADIO_BUTTON.find_me(driver).click()
    Body.CHECKBOX.find_me(driver).click()
    is_bike_selected = Body.CHECKBOX_BUTTON.find_me(driver)
    is_bike_selected.click()
    logging.info("Is bike option selected?")
    logging.info(is_bike_selected.is_selected())
    dropdown = Body.DROPDOWN_MENU.find_me(driver)
    dropdown.send_keys("Saab")
    logging.info("Is Saab selected?")
    logging.info(dropdown.is_selected())
    tab = Body.TAB_OPTION.find_me(driver)
    tab.click()
    logging.info("Is tab 1 selected?")
    logging.info(tab.is_selected())
    logging.info("Phase two - passed")


def test_down(driver):
    driver.get("https://ultimateqa.com/simple-html-elements-for-automation/")
    Footer.BUTTON_TOP_ON_GREY.find_me(driver).click()
    driver.back()
    Footer.BUTTON_SECOND_ON_GREY.find_me(driver).click()
    driver.back()
    Footer.BUTTON_THIRD_ON_GREY.find_me(driver).click()
    driver.back()
    Footer.BUTTON_LAST_ON_GREY.find_me(driver).click()
    driver.back()
    highlight_left = Footer.HIGHLIGHT_ME_LEFT.find_me(driver)
    action = ActionChains(driver)
    action.double_click(highlight_left).click().perform()
    highlight_middle = Footer.HIGHLIGHT_ME_MIDDLE.find_me(driver)
    action = ActionChains(driver)
    action.double_click(highlight_middle).click().perform()
    highlight_right = Footer.HIGHLIGHT_ME_RIGHT.find_me(driver)
    action = ActionChains(driver)
    action.double_click(highlight_right).click().perform()
    logging.info("Last phase - passed")
