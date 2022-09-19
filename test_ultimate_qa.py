from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
import pytest

driver = webdriver.Chrome(service=Service(r"C:\Program Files (x86)/chromedriver.exe"))


# For some reason this doesn't work, but without this "pytest" tests don't work, so I need to import it in some way.
# To solve this I have put its functionality in first and last tests
@pytest.fixture()
def test_setup():
    driver.implicitly_wait(10)
    driver.maximize_window()
    yield
    driver.close()
    driver.quit()
    print("Test completed")


# This test is about entering into a lot of links, so I made my life simpler, by making a function that waits for user
# to see what happened and then go back to the main site.
def go_back():
    time.sleep(1)
    driver.back()


# For each button or link I had to use specific selector that is why it is very diverse, even when it does not need to
# be.
def test_easy():
    driver.get("https://ultimateqa.com/simple-html-elements-for-automation/")
    driver.implicitly_wait(4)
    driver.maximize_window()
    simple = driver.find_element(By.ID, "button1")
    simple.click()
    go_back()
    simple = driver.find_element(By.ID, "button2")
    simple.click()
    go_back()
    time.sleep(1)
    simple = driver.find_element(By.ID, "idExample")
    simple.click()
    go_back()
    simple = driver.find_element(By.LINK_TEXT, "Click me using this link text!")
    simple.click()
    go_back()
    simple = driver.find_element(By.CLASS_NAME, "buttonClass")
    simple.click()
    go_back()
    simple = driver.find_element(By.NAME, "button1")
    simple.click()
    go_back()
    time.sleep(1)
    print("Phase one - passed")


# This one is more interesting. Except clicking into different links or buttons it's also sends some form and validates
# the options that were or were not chosen.
def test_mid():
    # this selector is huge, but that was the only way to make it work with pytest
    medium = driver.find_element(
        By.CSS_SELECTOR, "#post-909 > div > div.et-l.et-l--post > div >"
                         " div.et_pb_section.et_pb_section_2.et_section_regular > div"
                         " > div.et_pb_column.et_pb_column_1_3.et_pb_column_4.et_pb_css_mix_blend_mode_passthrough"
                         " > div.et_pb_module.et_pb_cta_0.et_pb_promo.et_pb_text_align_center.et_pb_bg_layout_dark "
                         "> div.et_pb_button_wrapper > a")
    medium.click()
    go_back()
    medium = driver.find_element(By.ID, "simpleElementsLink")
    medium.click()
    go_back()
    medium = driver.find_element(By.LINK_TEXT, "Clickable Icon")
    medium.click()
    go_back()
    medium = driver.find_element(
        By.XPATH, "/html/body/div[1]/div/div/div/article/div/div[1]"
                  "/div/div[3]/div/div[1]/div[5]/div/div[1]/a/span/span")
    medium.click()
    go_back()
    medium = driver.find_element(By.ID, "et_pb_contact_name_0")
    medium.send_keys("Hello")
    medium = driver.find_element(By.ID, "et_pb_contact_email_0")
    medium.send_keys("bb@cya.bye")
    time.sleep(1)
    medium = driver.find_element(By.NAME, "et_builder_submit_button")
    medium.click()
    time.sleep(3)
    medium = driver.find_element(
        By.XPATH, "/html/body/div[1]/div/div/div/article/div/div[1]"
                  "/div/div[3]/div/div[1]/div[7]/div/div/div/form/input[3]")
    medium.click()
    print(r"Is 'other' selected?")
    print(medium.is_selected())
    medium = driver.find_element(By.NAME, "vehicle")
    medium.click()
    print("Is bike option selected?")
    print(medium.is_selected())
    medium = driver.find_element(
        By.XPATH, "/html/body/div[1]/div/div/div/article/div/div[1]"
                  "/div/div[3]/div/div[1]/div[8]/div/div/div/form/input[2]")
    print("Is car option selected?")
    print(medium.is_selected())
    medium = driver.find_element(
        By.XPATH, "/html/body/div[1]/div/div/div/article/div/div[1]/div/div[3]"
                  "/div/div[1]/div[9]/div/div/div/select/option[@value='saab']")
    medium.click()
    print("Is Saab selected?")
    print(medium.is_selected())
    medium = driver.find_element(By.LINK_TEXT, "Tab 2")
    medium.click()
    print("Is tab 1 selected?")
    print(medium.is_selected())
    print("Phase two - passed")


# That is the last part. I was supposed to find elements via XPATH and then I had to highlight the "HIGHLIGHT ME" texts,
# and I thought that instead of click and drag it I want them to be highlighted separatedly.
def test_down():
    deep = driver.find_element(
        By.XPATH, "/html/body/div[1]/div/div/div/article/div/div[1]"
                  "/div/div[4]/div[1]/div/div[1]/div/div/div/form/button")
    deep.click()
    go_back()
    deep = driver.find_element(
        By.XPATH, "/html/body/div[1]/div/div/div/article/div/div[1]"
                  "/div/div[4]/div[1]/div/div[2]/div/div/div/form/button")
    deep.click()
    go_back()
    deep = driver.find_element(
        By.XPATH, "/html/body/div[1]/div/div/div/article/div/div[1]"
                  "/div/div[4]/div[2]/div/div[1]/div/div/div/form/button")
    deep.click()
    go_back()
    deep = driver.find_element(
        By.XPATH, "/html/body/div[1]/div/div/div/article/div/div[1]"
                  "/div/div[4]/div[2]/div/div[2]/div/div/div/form/button")
    deep.click()
    go_back()
    medium = driver.find_element(
        By.XPATH, "/html/body/div[1]/div/div/div/article/div/div[1]/div/div[5]/div/div[1]/div/div/div/h4/span")
    action = ActionChains(driver)
    action.double_click(medium).click().perform()
    time.sleep(1)
    medium = driver.find_element(
        By.XPATH, "/html/body/div[1]/div/div/div/article/div/div[1]/div/div[5]/div/div[2]/div/div/div/h4/span")
    action = ActionChains(driver)
    action.double_click(medium).click().perform()
    time.sleep(1)
    medium = driver.find_element(
        By.XPATH, "/html/body/div[1]/div/div/div/article/div/div[1]/div/div[5]/div/div[3]/div/div/div/h4/span")
    action = ActionChains(driver)
    action.double_click(medium).click().perform()
    time.sleep(2)
    print("Phase three - passed")
    # driver.quit()


# This one worked properly, but without logical reason the login screen started to send CAPTCHA, so I keep it censored
# in case it might start to work properly again.
def test_login():
    log = driver.find_element(By.LINK_TEXT, "Go to login page")
    log.click()
    driver.implicitly_wait(5)
    log = driver.find_element(By.ID, "user[email]")
    log.send_keys("booboo@gj.bro")
    log = driver.find_element(By.ID, "user[password]")
    log.send_keys("booboo@gj.bro")
    log = driver.find_element(By.ID, "user[remember_me]")
    log.click()
    log = driver.find_element(By.XPATH, "/html/body/main/div/div/article/form/div[4]/input")
    log.click()
    time.sleep(2)
    log = driver.find_element(By.LINK_TEXT, "Forgot Password?")
    log.click()
    driver.implicitly_wait(3)
    log = driver.find_element(By.ID, "user[email]")
    log.send_keys("booboo@gj.bro")
    log = driver.find_element(By.NAME, "commit")
    log.click()
    time.sleep(2)
    driver.quit()
    print("Last phase - passed")
