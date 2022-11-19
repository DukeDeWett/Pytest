from selenium.webdriver.common.by import By


class Body:
    BUTTON_SIMPLE_CONTROLS = By.XPATH, "//a[@href='/button-success'][@class='et_pb_button et_pb_promo_button']"
    CLICK_THIS_LINK = By.ID, "simpleElementsLink"
    ICON_CLICKABLE_TEXT = By.LINK_TEXT, "Clickable Icon"
    ICON_CLICKABLE_ARROW = By.XPATH, "//span[@class='et_pb_image_wrap']"
    NAME = By.ID, "et_pb_contact_name_0"
    MAIL = By.ID, "et_pb_contact_email_0"
    BUTTON_EMAIL_ME = By.NAME, "et_builder_submit_button"
    KEY1 = "Hello"
    KEY2 = "bb@cya.bye"
    RADIO_BUTTON = By.XPATH, "//input[@type='radio'][@value='male']"
    CHECKBOX = By.NAME, "vehicle"
    CHECKBOX_BUTTON = By.XPATH, "//input[@type='checkbox'][@value='Car']"
    DROPDOWN_MENU = By.XPATH, "//select"
    TAB_OPTION = By.XPATH, "//a[@href='#']"
    CAR_OPTION = "Saab"
