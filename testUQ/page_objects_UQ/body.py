from selenium.webdriver.common.by import By


class Body:
    BUTTON1 = By.XPATH, "//*[@id='post-909']/div/div[1]/div/div[3]/div/div[1]/div[2]/div[2]/a"
    LINK1 = By.ID, "simpleElementsLink"
    ICON1 = By.LINK_TEXT, "Clickable Icon"
    ICON2 = By.XPATH, "//*[@id='post-909']/div/div[1]/div/div[3]/div/div[1]/div[5]/div/div[1]"
    NAME = By.ID, "et_pb_contact_name_0"
    MAIL = By.ID, "et_pb_contact_email_0"
    RADIO = By.NAME, "et_builder_submit_button"
    KEY1 = By.XPATH, "Hello"
    KEY2 = By.NAME, "bb@cya.bye"
    RADIO1 = By.XPATH, "//*[@id='post-909']/div/div[1]/div/div[3]/div/div[1]/div[7]/div/div/div/form/input[1]"
    CHECKBOX = By.NAME, "vehicle"
    CHECKBOX2 = By.XPATH, "//*[@id='post-909']/div/div[1]/div/div[3]/div/div[1]/div[8]/div/div/div/form/input[2]"
    DROPDOWN = By.XPATH, "//*[@id='post-909']/div/div[1]/div/div[3]/div/div[1]/div[9]/div/div/div/select"
    TAB = By.XPATH, "//*[@id='post-909']/div/div[1]/div/div[3]/div/div[1]/div[10]/ul/li[1]/a"
    BUTTON2 = By.NAME, "et_builder_submit_button"
    CAR = "Saab"
