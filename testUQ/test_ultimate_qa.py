import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from page_objects_UQ.ultimate_qa import HomePage
import logging

driver = webdriver.Chrome(service=Service(r"C:\Program Files (x86)/chromedriver.exe"))  # This is a typical path for
# Windows, if there is a need to make it work on other operating systems it can be done with 'if' statements for example
logging.basicConfig(level=logging.NOTSET)


def go_back():
    driver.implicitly_wait(5)
    driver.back()


def wait():
    driver.implicitly_wait(5)


class TestUQ:
    @pytest.fixture(scope='module')
    def start(self):
        driver.get("https://ultimateqa.com/simple-html-elements-for-automation/")
        wait()
        driver.maximize_window()
        yield
        logging.info("Tests completed!")
        driver.quit()

    # For each button or link I had to use specific selector that is why it is very diverse, even when it does not need
    # to be.
    def test_easy(self, start):
        wait()
        driver.find_element(By.ID, HomePage.b1).click()
        go_back()
        driver.find_element(By.ID, HomePage.b2).click()
        go_back()
        wait()
        driver.find_element(By.ID, HomePage.b3).click()
        go_back()
        driver.find_element(By.LINK_TEXT, HomePage.link).click()
        go_back()
        driver.find_element(By.CLASS_NAME, HomePage.button).click()
        go_back()
        driver.find_element(By.NAME, HomePage.button1).click()
        go_back()
        wait()
        logging.info("Phase one - passed")

    # This one is more interesting. Except clicking into different links or buttons it's also sends some
    # form and validates the options that were or were not chosen.
    def test_mid(self):
        # this selector is huge, but that was the only way to make it work with selenium
        driver.find_element(By.XPATH, HomePage.button2).click()
        go_back()
        driver.find_element(By.ID, HomePage.link1).click()
        go_back()
        driver.find_element(By.LINK_TEXT, HomePage.icon).click()
        go_back()
        driver.find_element(By.XPATH, HomePage.icon1).click()
        go_back()
        driver.find_element(By.ID, HomePage.name).send_keys(HomePage.key1)
        driver.find_element(By.ID, HomePage.mail).send_keys(HomePage.key2)
        wait()
        driver.find_element(By.NAME, HomePage.radio).click()
        wait()
        medium = driver.find_element(By.XPATH, HomePage.radio1)
        medium.click()
        wait()
        logging.info(r"Is 'other' selected?")
        logging.info(medium.is_selected())
        medium = driver.find_element(By.NAME, HomePage.checkbox)
        wait()
        medium.click()
        logging.info("Is bike option selected?")
        logging.info(medium.is_selected())
        medium = driver.find_element(By.XPATH, HomePage.checkbox2)
        wait()
        logging.info("Is car option selected?")
        logging.info(medium.is_selected())
        medium = driver.find_element(By.XPATH, HomePage.dropdown)
        wait()
        medium.click()
        logging.info("Is Saab selected?")
        logging.info(medium.is_selected())
        medium = driver.find_element(By.LINK_TEXT, HomePage.tab)
        wait()
        medium.click()
        logging.info("Is tab 1 selected?")
        logging.info(medium.is_selected())
        logging.info("Phase two - passed")
        wait()

    # That is the last part. I was supposed to find elements via XPATH, and then I had to highlight the "HIGHLIGHT ME"
    # texts, and I thought that instead of click and drag it I want them to be highlighted separately.
    def test_down(self):
        driver.find_element(By.XPATH, HomePage.button3).click()
        go_back()
        driver.find_element(By.XPATH, HomePage.button4).click()
        go_back()
        driver.find_element(By.XPATH, HomePage.button5).click()
        go_back()
        driver.find_element(By.XPATH, HomePage.button6).click()
        go_back()
        medium = driver.find_element(By.XPATH, HomePage.highlight)
        wait()
        action = ActionChains(driver)
        action.double_click(medium).click().perform()
        medium = driver.find_element(By.XPATH, HomePage.highlight1)
        wait()
        action = ActionChains(driver)
        action.double_click(medium).click().perform()
        medium = driver.find_element(By.XPATH, HomePage.highlight2)
        wait()
        action = ActionChains(driver)
        action.double_click(medium).click().perform()
        logging.info("Phase three - passed")

    # def test_login(self):
    #     driver.find_element(By.LINK_TEXT, HomePage.link2).click()
    #     wait()
    #     driver.find_element(By.ID, HomePage.key3).send_keys("booboo@gj.bro")
    #     wait()
    #     driver.find_element(By.ID, HomePage.key4).send_keys("booboo@gj.bro")
    #     wait()
    #     driver.find_element(By.ID, HomePage.button7).click()
    #     wait()
    #     driver.find_element(By.XPATH, HomePage.button8).click()
    #     wait()
    #     driver.find_element(By.LINK_TEXT, HomePage.link3).click()
    #     wait()
    #     driver.find_element(By.NAME, HomePage.button9).click()
    #     wait()
    #     logging.info("Last phase - passed")

    @pytest.fixture
    def close_msg(self):
        logging.info("Bye, bye")
