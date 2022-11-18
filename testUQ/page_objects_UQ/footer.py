from selenium.webdriver.common.by import By


class Footer:
    BUTTON1 = By.XPATH, "//*[@id='button1']"
    BUTTON2 = By.XPATH, "/html/body/div[1]/div/div/div/article/div/div[1]/div/div[4]/div[1]/div/div[2]/div/div/div" \
                        "/form/button"
    BUTTON3 = By.XPATH, "//*[@id='button1' and text()='Xpath Button 1']"
    BUTTON4 = By.XPATH, "//*[@id='button1' and text()='Xpath Button 2']"
    HIGHLIGHT1 = By.XPATH, "//*[@id='post-909']/div/div[1]/div/div[5]/div/div[1]/div/div/div/h4/span"
    HIGHLIGHT2 = By.XPATH, "//*[@id='post-909']/div/div[1]/div/div[5]/div/div[2]/div/div/div/h4/span"
    HIGHLIGHT3 = By.XPATH, "//*[@id='post-909']/div/div[1]/div/div[5]/div/div[3]/div/div/div/h4/span"
