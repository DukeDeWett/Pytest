from selenium.webdriver.common.by import By


class Header:
    BUTTON1 = By.ID, "button1"
    BUTTON2 = By.ID, 'button2'
    BUTTON3 = By.ID, "idExample"
    LINK1 = By.LINK_TEXT, "Click me using this link text!"
    BUTTON4 = By.CLASS_NAME, "buttonClass"
    BUTTON5 = By.NAME, "button1"
