from selenium.webdriver.common.by import By
from page_objects_UQ.base_page_object import BasePageObject


class Footer(BasePageObject):
    BUTTON_TOP_ON_GREY = By.XPATH, "//*[@id='button1']"
    BUTTON_SECOND_ON_GREY = By.XPATH, "(//button[@id='button1'])[2]"
    BUTTON_THIRD_ON_GREY = By.XPATH, "//*[@id='button1' and text()='Xpath Button 1']"
    BUTTON_LAST_ON_GREY = By.XPATH, "//*[@id='button1' and text()='Xpath Button 2']"
    HIGHLIGHT_ME_LEFT = By.XPATH, "//span[text()='Highlight me']"
    HIGHLIGHT_ME_MIDDLE = By.XPATH, "(//span[text()='Highlight me'])[2]"
    HIGHLIGHT_ME_RIGHT = By.XPATH, "(//span[text()='Highlight me'])[3]"
