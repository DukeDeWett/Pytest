from enum import Enum
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BasePageObject(Enum):
    @property
    def by(self):
        return self.value[0]

    @property
    def locator(self):
        return self.value[1]

    def find_me(self, driver):
        return WebDriverWait(driver=driver, timeout=30).until(ec.element_to_be_clickable(self.value))
