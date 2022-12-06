from selenium.webdriver.common.by import By
from enum import Enum


class BasePageObject(Enum):
    @property
    def by(self):
        return self.value[1]

    @property
    def locator(self):
        return self.value[0]

    def find_element(self, driver):
        return f"{self.locator} {self.by} {driver}"


class Header(BasePageObject):
    BUTTON_CLICK_ME = By.ID, "button1"
    BUTTON_RAISE = By.ID, 'button2'
    BUTTON_GREEN_ID = By.ID, "idExample"
    LINK_ON_BLUE = By.LINK_TEXT, "Click me using this link text!"
    BUTTON_CLASS_NAME_ON_BLUE = By.CLASS_NAME, "buttonClass"
    BUTTON_NAME_ON_BLUE = By.NAME, "button1"
