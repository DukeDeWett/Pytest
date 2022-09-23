from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import Select
import time
import pytest
import os

driver = webdriver.Chrome(service=Service(r"C:\Program Files (x86)/chromedriver.exe"))


# For some reason this doesn't work, but without this "pytest" tests don't work, so I need to import it in some way.
# To solve this I have put its functionality in first and last tests
@pytest.fixture()
def test_setup():
    driver.get("https://demoqa.com/elements")
    driver.implicitly_wait(10)
    driver.maximize_window()
    yield
    driver.close()
    driver.quit()
    print("Test completed")


def test_text_box():
    driver.get("https://demoqa.com/elements")
    driver.maximize_window()
    driver.implicitly_wait(5)
    driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div[1]/div/div/div[1]/div/ul/li[1]/span").click()
    ele = driver.find_element(By.ID, "userName")
    ele.send_keys("User")
    ele = driver.find_element(By.ID, "userEmail")
    ele.send_keys("User@name.com")
    ele = driver.find_element(By.ID, "currentAddress")
    ele.send_keys("Lazytown 66/6 Ohio")
    ele = driver.find_element(By.ID, "permanentAddress")
    ele.send_keys("Lazytown 66/6 Ohio")
    ele = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div[2]/div[2]/form/div[5]/div/button")
    action = ActionChains(driver)
    action.click_and_hold(ele).perform()
    ele.send_keys(Keys.ENTER)
    time.sleep(2)


def test_check_box():
    driver.implicitly_wait(3)
    driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div[1]/div/div/div[1]/div/ul/li[2]/span").click()
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, "#tree-node > ol > li > span > label > span.rct-checkbox > svg").click()
    time.sleep(2)


def test_radio_button():
    driver.implicitly_wait(3)
    driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div[1]/div/div/div[1]/div/ul/li[3]/span").click()
    try:
        ele = WebDriverWait(driver, 10).until(
            ec.presence_of_element_located((By.CSS_SELECTOR, "#yesRadio"))
        )
        webdriver.ActionChains(driver).move_to_element(ele).click(ele).perform()
    finally:
        pass
    time.sleep(2)


# On this table I added new user, edited the existed one, used search bar to find specific user, and I deleted him.
def test_web_tables():
    driver.implicitly_wait(3)
    driver.find_element(By.CSS_SELECTOR, "#item-3 > svg").click()
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, "#addNewRecordButton").click()
    time.sleep(1)
    ele = driver.find_element(By.ID, "firstName")
    ele.send_keys("Mark")
    ele = driver.find_element(By.ID, "lastName")
    ele.send_keys("Karm")
    ele = driver.find_element(By.ID, "userEmail")
    ele.send_keys("Mark@op.gg")
    ele = driver.find_element(By.ID, "age")
    ele.send_keys("33")
    ele = driver.find_element(By.ID, "salary")
    ele.send_keys("2600")
    ele = driver.find_element(By.ID, "department")
    ele.send_keys("Legal")
    ele.send_keys(Keys.ENTER)
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, "#edit-record-2 > svg > path").click()
    ele = driver.find_element(By.ID, "salary")
    ele.send_keys(Keys.CONTROL+"A")
    time.sleep(1)
    ele.send_keys(Keys.DELETE)
    ele.send_keys("14000")
    time.sleep(1)
    ele.send_keys(Keys.ENTER)
    time.sleep(1)
    ele = driver.find_element(By.ID, "searchBox")
    ele.send_keys("Vega")
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, "#delete-record-1 > svg > path").click()
    print("Cierra Vega removed!")
    time.sleep(1)


# This tests is made to click each button in a specific way.
def test_buttons():
    ele = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div[1]/div/div/div[1]/div/ul/li[5]")
    driver.execute_script("arguments[0].click();", ele)
    action = ActionChains(driver)
    ele = driver.find_element(By.ID, "doubleClickBtn")
    action.double_click(ele).perform()
    ele = driver.find_element(By.ID, "rightClickBtn")
    action.context_click(ele).perform()
    ele = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div[2]/div[2]/div[3]/button")
    driver.execute_script("arguments[0].click();", ele)
    time.sleep(2)


def test_links():
    driver.implicitly_wait(5)
    ele = driver.find_element(By.CSS_SELECTOR, "#item-5 > span")
    driver.execute_script("arguments[0].click();", ele)
    driver.find_element(By.ID, "simpleLink").click()
    time.sleep(2)
    page = driver.window_handles[1]
    driver.switch_to.window(page)
    driver.close()
    time.sleep(2)
    windows = driver.window_handles
    driver.switch_to.window(windows[0])
    time.sleep(1)
    driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div[2]/div[2]/p[2]/a").click()
    time.sleep(2)
    page = driver.window_handles[1]
    driver.switch_to.window(page)
    driver.close()
    time.sleep(2)
    windows = driver.window_handles
    driver.switch_to.window(windows[0])
    ele = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div[2]/div[2]/p[8]/a")
    driver.execute_script("arguments[0].click();", ele)
    time.sleep(2)
    print("Link has responded with status 403 and status text Forbidden")


def test_broken_link():
    driver.implicitly_wait(5)
    ele = driver.find_element(By.CSS_SELECTOR, "#item-6 > span")
    driver.execute_script("arguments[0].click();", ele)
    ele = driver.find_element(By.LINK_TEXT, "Click Here for Valid Link")
    driver.execute_script("arguments[0].click();", ele)
    time.sleep(2)
    driver.back()
    ele = driver.find_element(By.LINK_TEXT, "Click Here for Broken Link")
    driver.execute_script("arguments[0].click();", ele)
    time.sleep(2)
    ele = driver.find_element(By.LINK_TEXT, "here")
    driver.execute_script("arguments[0].click();", ele)
    time.sleep(2)
    driver.back()
    driver.back()
    time.sleep(1)


def test_upload_and_download():
    driver.implicitly_wait(3)
    ele = driver.find_element(By.CSS_SELECTOR, "#item-7 > span")
    driver.execute_script("arguments[0].click();", ele)
    driver.find_element(By.ID, "downloadButton").click()
    driver.implicitly_wait(2)
    driver.find_element(By.ID, "uploadFile").send_keys(os.getcwd() + "/sampleFile.jpeg")
    time.sleep(2)


def test_dynamic_properties():
    driver.implicitly_wait(3)
    ele = driver.find_element(By.CSS_SELECTOR, "#item-8 > span")
    driver.execute_script("arguments[0].click();", ele)
    ele = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div[2]/div[2]/p")
    action = ActionChains(driver)
    action.double_click(ele).click().perform()
    try:
        ele = WebDriverWait(driver, 10).until(
            ec.presence_of_element_located((By.ID, "visibleAfter"))
        )
        webdriver.ActionChains(driver).move_to_element(ele).double_click().perform()
    finally:
        pass
    print("Visible after 5 seconds button clicked.")
    print("Elements part finished.")


# Unfortunately it is almost impossible to see bottom part of this, because of big AD, but believe it worked.:)
def test_practice_form():
    driver.implicitly_wait(3)
    driver.find_element(By.CSS_SELECTOR, "#app > div > div > div.row > div:nth-child(1) > "
                                         "div > div > div:nth-child(1) > span"
                                         " > div > div.header-text").click()
    driver.implicitly_wait(3)
    ele = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div[1]/div/div/div[2]/div/ul/li/span")
    driver.execute_script("arguments[0].click();", ele)
    driver.find_element(By.ID, "firstName").send_keys("Mariano")
    driver.find_element(By.ID, "lastName").send_keys("Italiano")
    driver.find_element(By.ID, "userEmail").send_keys("Mariano@liano.ita")
    ele = driver.find_element(By.ID, "gender-radio-1")
    driver.execute_script("arguments[0].click();", ele)
    driver.find_element(By.ID, "userNumber").send_keys("2193000022")
    ele = driver.find_element(By.ID, "dateOfBirthInput")
    action = ActionChains(driver)
    action.double_click(ele).click().perform()
    ele.send_keys("12 SEP 2001")
    ele.send_keys(Keys.ENTER)
    try:
        ele = WebDriverWait(driver, 10).until(
            ec.presence_of_element_located((By.XPATH, "//input[@id='subjectsInput']"))
        )
        ele.send_keys("History")
        ele.send_keys(Keys.TAB)
    finally:
        pass
    ele = driver.find_element(By.ID, "hobbies-checkbox-2")
    driver.execute_script("arguments[0].click();", ele)
    driver.execute_script("window.scrollBy(0,400)", "")
    driver.implicitly_wait(2)
    driver.find_element(By.ID, "uploadPicture").send_keys(os.getcwd() + "/sampleFile.jpeg")
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, "#currentAddress").send_keys("7460 West Lafayette Ave. Dedham, MA 02026")
    driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div[2]/div[2]/form/div[10]/div[2]/div/div"
                                  "/div[1]/div[2]/div/input").send_keys("NCR", Keys.ENTER)
    time.sleep(1)
    driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div[2]/div[2]/form/div[10]/div[3]/div"
                                  "/div/div[1]/div[2]/div/input").send_keys("Gurgaon", Keys.ENTER)
    time.sleep(1)
    ele = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div[2]/div[2]/form/div[11]/div/button")
    driver.execute_script("arguments[0].click();", ele)
    time.sleep(2)
    try:
        ele = WebDriverWait(driver, 10).until(
            ec.presence_of_element_located((By.CSS_SELECTOR, "#closeLargeModal"))
        )
        driver.execute_script("arguments[0].click();", ele)
    finally:
        pass
    print("Form sent succesfully!")


def test_browser_window():
    driver.implicitly_wait(3)
    ele = driver.find_element(By.CSS_SELECTOR, "#app > div > div"
                                               " > div.row > div:nth-child(1) > div > div > div:nth-child(3)"
                                               "> span > div > div.header-text")
    driver.execute_script("arguments[0].click();", ele)
    driver.implicitly_wait(3)
    ele = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div[1]/div/div/div[3]/div/ul/li[1]/span")
    driver.execute_script("arguments[0].click();", ele)
    driver.implicitly_wait(3)
    driver.find_element(By.ID, "tabButton").click()
    time.sleep(2)
    page = driver.window_handles[1]
    driver.switch_to.window(page)
    driver.close()
    time.sleep(2)
    driver.switch_to.window(driver.window_handles[0])
    ele = driver.find_element(By.ID, "windowButton")
    driver.execute_script("arguments[0].click();", ele)
    driver.implicitly_wait(3)
    driver.switch_to.window(driver.window_handles[1])
    time.sleep(1)
    driver.close()
    time.sleep(0.5)
    driver.switch_to.window(driver.window_handles[0])
    ele = driver.find_element(By.CSS_SELECTOR, "#messageWindowButton")
    driver.execute_script("arguments[0].click();", ele)
    time.sleep(1)
    driver.switch_to.window(driver.window_handles[1])
    time.sleep(1)
    driver.close()
    time.sleep(0.9)
    driver.switch_to.window(driver.window_handles[0])
    time.sleep(1)


def test_alerts():
    driver.implicitly_wait(3)
    ele = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div[1]/div/div/div[3]/div/ul/li[2]")
    driver.execute_script("arguments[0].click();", ele)
    driver.implicitly_wait(2)
    driver.find_element(By.ID, "alertButton").click()
    time.sleep(1)
    Alert(driver).accept()
    driver.find_element(By.ID, "timerAlertButton").click()
    try:
        WebDriverWait(driver, 10).until(ec.alert_is_present(), 'Timed out waiting for alerts to appear')
        time.sleep(1)
        Alert(driver).accept()
    finally:
        print("Alert correctly accepted.")
    driver.find_element(By.ID, "confirmButton").click()
    time.sleep(1)
    Alert(driver).accept()
    driver.find_element(By.ID, "promtButton").click()
    time.sleep(1)
    Alert(driver).send_keys("easy")
    Alert(driver).accept()
    time.sleep(1)


def test_frames():
    driver.implicitly_wait(3)
    ele = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div[1]/div/div/div[3]/div/ul/li[3]")
    driver.execute_script("arguments[0].click();", ele)
    iframe = driver.find_element(By.XPATH, "/html")
    driver.switch_to.frame(iframe)
    iframe.send_keys("Hello there!")
    time.sleep(2)
    driver.switch_to.default_content()
    print("You successfully switched between iframe and parent frame!")
    time.sleep(1)


def test_modal_dialogs():
    driver.implicitly_wait(2)
    ele = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div[1]/div/div/div[3]/div/ul/li[5]/span")
    driver.execute_script("arguments[0].click();", ele)
    ele = driver.find_element(By.ID, "showSmallModal")
    driver.execute_script("arguments[0].click();", ele)
    time.sleep(0.9)
    WebDriverWait(driver, 20).until(ec.element_to_be_clickable(
        (By.CSS_SELECTOR, "#closeSmallModal"))).click()
    time.sleep(0.5)
    ele = driver.find_element(By.ID, "showLargeModal")
    driver.execute_script("arguments[0].click();", ele)
    time.sleep(2)
    WebDriverWait(driver, 20).until(ec.element_to_be_clickable(
        (By.CSS_SELECTOR, "#closeLargeModal"))).click()
    time.sleep(1)


def test_accordians():
    driver.implicitly_wait(2)
    ele = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div[1]/div/div/div[4]/div/ul/li[1]")
    driver.execute_script("arguments[0].click();", ele)
    time.sleep(2)
    driver.execute_script("window.scrollBy(0,300)", "")
    ele = driver.find_element(By.CSS_SELECTOR, "#section2Heading")
    driver.execute_script("arguments[0].click();", ele)
    time.sleep(2)
    ele = driver.find_element(By.CSS_SELECTOR, "#section3Heading")
    driver.execute_script("arguments[0].click();", ele)
    time.sleep(2)


def test_auto_complete():
    driver.implicitly_wait(2)
    ele = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div[1]/div/div/div[4]/div/ul/li[2]/span")
    driver.execute_script("arguments[0].click();", ele)
    time.sleep(1)
    ele = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div[2]/div[2]/div[1]/div/div/div/div/div[1]"
                                        "/div[2]/div/input")
    ele.send_keys("Indigo")
    ele.send_keys(Keys.ENTER)
    time.sleep(0.5)
    ele.send_keys("Purple")
    ele.send_keys(Keys.ENTER)
    time.sleep(1)
    ele = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div[2]/div[2]/div[2]/div/div/div/div/div[1]"
                                        "/div[2]/div/input")
    ele.send_keys("Red")
    ele.send_keys(Keys.ENTER)
    time.sleep(1)


def test_date_picker():
    driver.implicitly_wait(3)
    ele = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div[1]/div/div/div[4]/div/ul/li[3]/span")
    driver.execute_script("arguments[0].click();", ele)
    ele = WebDriverWait(driver, 10).until(
                ec.visibility_of_element_located((By.XPATH, "/html/body/div[2]/div/div/div[2]"
                                                            "/div[2]/div[2]/div[1]/div[2]/div[1]/div/input")))
    ele.send_keys(Keys.CONTROL + "a")
    ele.send_keys(Keys.DELETE)
    ele.send_keys("9/10/2005")
    ele.send_keys(Keys.ENTER)
    time.sleep(0.9)
    ele = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div[2]/div[2]/div[2]/div[2]/div[1]/div/input")
    ele.send_keys(Keys.CONTROL + "a")
    ele.send_keys(Keys.DELETE)
    ele.send_keys("October 9, 2005 3:33")
    ele.send_keys(Keys.ENTER)
    time.sleep(0.9)


def test_sliders():
    ele = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div[1]/div/div/div[4]/div/ul/li[4]")
    driver.execute_script("arguments[0].click();", ele)
    time.sleep(1)
    ele = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div[2]/form/div/div[1]/span/input")
    move = ActionChains(driver)
    move.click_and_hold(ele).move_by_offset(78, 0).release().perform()
    time.sleep(1)
    move.click_and_hold(ele).move_by_offset(10, 0).release().perform()
    time.sleep(1)
    move.click_and_hold(ele).move_by_offset(150, 0).release().perform()


def test_progress_bar():
    driver.implicitly_wait(2)
    ele = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div[1]/div/div/div[4]/div/ul/li[5]")
    driver.execute_script("arguments[0].click();", ele)
    ele = WebDriverWait(driver, 10).until(
        ec.visibility_of_element_located((By.XPATH, "//*[@id='startStopButton']")))
    ele.click()
    time.sleep(1.4)
    ele.click()
    time.sleep(1.4)
    driver.execute_script("arguments[0].click();", ele)
    ele = WebDriverWait(driver, 20).until(
        ec.visibility_of_element_located((By.ID, "resetButton")))
    time.sleep(1)
    ele.click()
    time.sleep(1)


def test_tabs():
    ele = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div[1]/div/div/div[4]/div/ul/li[6]")
    driver.execute_script("arguments[0].click();", ele)
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, "#demo-tab-origin").click()
    driver.execute_script("window.scrollBy(0,300)", "")
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, "#demo-tab-use").click()
    time.sleep(2)
    ele = driver.find_element(By.CSS_SELECTOR, "#demo-tab-more")
    if ele.is_enabled() is False:
        ele.click()
    else:
        print("Last tab is disabled like intended.")


def test_tool_tips():
    ele = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div[1]/div/div/div[4]/div/ul/li[7]/span")
    driver.execute_script("arguments[0].click();", ele)
    ele = driver.find_element(By.XPATH, "//*[@id='toolTipButton']")
    ActionChains(driver).move_to_element(ele).perform()
    time.sleep(1)
    ele = driver.find_element(By.ID, "toolTipTextField")
    ActionChains(driver).move_to_element(ele).perform()
    time.sleep(1)
    ele = driver.find_element(By.XPATH, "// *[ @ id = 'texToolTopContainer']/a[1]")
    ActionChains(driver).move_to_element(ele).perform()
    time.sleep(1)
    driver.execute_script("window.scrollBy(0,100)", "")
    ele = driver.find_element(By.XPATH, "//*[@id='texToolTopContainer']/a[2]")
    ActionChains(driver).move_to_element(ele).perform()
    time.sleep(1)


def test_menu():
    driver.implicitly_wait(3)
    ele = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div[1]/div/div/div[4]/div/ul/li[8]/span")
    driver.execute_script("arguments[0].click();", ele)
    ele = driver.find_element(By.XPATH, "//*[@id='nav']/li[1]/a")
    ActionChains(driver).move_to_element(ele).perform()
    time.sleep(0.9)
    ele = driver.find_element(By.XPATH, "//*[@id='nav']/li[3]/a")
    ActionChains(driver).move_to_element(ele).perform()
    time.sleep(0.9)
    driver.find_element(By.XPATH, "//*[@id='nav']/li[2]/a").click()
    time.sleep(0.9)
    ele = driver.find_element(By.XPATH, "//*[@id='nav']/li[2]/ul/li[2]/a")
    ActionChains(driver).move_to_element(ele).perform()
    time.sleep(0.9)
    ele = driver.find_element(By.XPATH, "//*[@id='nav']/li[2]/ul/li[3]/a")
    ActionChains(driver).move_to_element(ele).perform()
    time.sleep(0.9)
    ele = driver.find_element(By.XPATH, "//*[@id='nav']/li[2]/ul/li[3]/ul/li[2]/a")
    ActionChains(driver).move_to_element(ele).perform()
    time.sleep(0.9)


def test_select_menu():
    driver.implicitly_wait(3)
    ele = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div[1]/div/div/div[4]/div/ul/li[9]/span")
    driver.execute_script("arguments[0].click();", ele)
    driver.implicitly_wait(2)
    ele = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH,
                                                                      "/html/body/div[2]/div/div/div[2]/div[2]/div[2]"
                                                                      "/div[2]/div/div/div/div[1]/div[2]/div/input")))
    ele.send_keys("Group 1, option 1" + Keys.ENTER)
    time.sleep(0.7)
    ele = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.XPATH,
                                                                      "/html/body/div[2]/div/div/div[2]/div[2]/div[2]"
                                                                      "/div[4]/div/div/div/div[1]/div[2]/div/input")))
    ele.send_keys("Prof." + Keys.ENTER)
    time.sleep(0.7)
    driver.find_element(By.CSS_SELECTOR, "#oldSelectMenu")
    Select(driver.find_element(By.CSS_SELECTOR, "#oldSelectMenu")).select_by_visible_text("Indigo")
    time.sleep(0.7)
    driver.execute_script("window.scrollBy(0,300)", "")
    ele = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div[2]/div[2]/div[7]/div/div/div/div[1]"
                                        "/div[2]/div/input")
    ele.send_keys("Black")
    ele.send_keys(Keys.TAB)
    time.sleep(0.7)
    ele.send_keys("Red")
    ele.send_keys(Keys.TAB)
    time.sleep(1)
    Select(driver.find_element(By.CSS_SELECTOR, "#cars")).select_by_visible_text("Saab")
    Select(driver.find_element(By.CSS_SELECTOR, "#cars")).select_by_visible_text("Volvo")
    time.sleep(0.7)


def test_sortable():
    driver.get("https://demoqa.com/elements")
    driver.implicitly_wait(5)
    driver.maximize_window()
    ele = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div[1]/div/div/div[5]/div/ul/li[1]/span")
    driver.execute_script("arguments[0].click();", ele)
    driver.execute_script("window.scrollBy(0,300)", "")
    time.sleep(1)
    ele = driver.find_element(By.XPATH, "//*[@id='demo-tabpane-list']/div/div[1]")
    move = ActionChains(driver)
    move.click_and_hold(ele).move_by_offset(0, 100).release().perform()
    time.sleep(1)
    ele = driver.find_element(By.XPATH, "//*[@id='demo-tabpane-list']/div/div[6]")
    move = ActionChains(driver)
    move.click_and_hold(ele).move_by_offset(0, -100).release().perform()
    time.sleep(1)
    driver.find_element(By.ID, "demo-tab-grid").click()
    ele = driver.find_element(By.XPATH, "//*[@id='demo-tabpane-grid']/div/div/div[5]")
    time.sleep(1)
    move = ActionChains(driver)
    move.click_and_hold(ele).move_by_offset(100, 150).release().perform()
    time.sleep(1)
    ele = driver.find_element(By.XPATH, "//*[@id='demo-tabpane-grid']/div/div/div[2]")
    move = ActionChains(driver)
    move.click_and_hold(ele).move_by_offset(50, 100).release().perform()
    time.sleep(1)
    ele = driver.find_element(By.XPATH, "//*[@id='demo-tabpane-grid']/div/div/div[8]")
    move = ActionChains(driver)
    move.click_and_hold(ele).move_by_offset(-100, -50).release().perform()
    time.sleep(1)


def test_selectable():
    ele = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div[1]/div/div/div[5]/div/ul/li[2]/span")
    driver.execute_script("arguments[0].click();", ele)
    time.sleep(1)
    ele = driver.find_element(By.CSS_SELECTOR, "#verticalListContainer > li:nth-child(4)")
    driver.execute_script("arguments[0].click();", ele)
    time.sleep(1)
    ele = driver.find_element(By.CSS_SELECTOR, "#verticalListContainer > li:nth-child(2)")
    driver.execute_script("arguments[0].click();", ele)
    time.sleep(1)
    ele = driver.find_element(By.CSS_SELECTOR, "#verticalListContainer > li:nth-child(1)")
    driver.execute_script("arguments[0].click();", ele)
    time.sleep(1)
    ele = driver.find_element(By.CSS_SELECTOR, "#verticalListContainer > li:nth-child(3)")
    driver.execute_script("arguments[0].click();", ele)
    time.sleep(1)
    ele = driver.find_element(By.CSS_SELECTOR, "#verticalListContainer > li:nth-child(4)")
    driver.execute_script("arguments[0].click();", ele)
    time.sleep(1)
    driver.find_element(By.ID, "demo-tab-grid").click()
    driver.execute_script("window.scrollBy(0,300)", "")
    time.sleep(0.5)
    driver.find_element(By.CSS_SELECTOR, "#row1 > li:nth-child(1)").click()
    time.sleep(0.5)
    driver.find_element(By.CSS_SELECTOR, "#row1 > li:nth-child(3)").click()
    time.sleep(0.5)
    driver.find_element(By.CSS_SELECTOR, "#row2 > li:nth-child(2)").click()
    time.sleep(0.5)
    driver.find_element(By.CSS_SELECTOR, "#row3 > li:nth-child(1)").click()
    time.sleep(0.5)
    driver.find_element(By.CSS_SELECTOR, "#row3 > li:nth-child(3)").click()
    time.sleep(1)


def test_resizable():
    driver.implicitly_wait(2)
    ele = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div[1]/div/div/div[5]/div/ul/li[3]")
    driver.execute_script("arguments[0].click();", ele)
    time.sleep(1)
    driver.execute_script("window.scrollBy(0,300)", "")
    ele = driver.find_element(By.XPATH, "//*[@id='resizableBoxWithRestriction']/span")
    move = ActionChains(driver)
    move.click_and_hold(ele).move_by_offset(100, 100).release().click().perform()
    time.sleep(1)


def test_droppable():
    driver.implicitly_wait(2)
    ele = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div[1]/div/div/div[5]/div/ul/li[4]/span")
    driver.execute_script("arguments[0].click();", ele)
    time.sleep(0.7)
    ele = driver.find_element(By.ID, "draggable")
    move = ActionChains(driver)
    move.click_and_hold(ele).move_by_offset(270, 0).release().perform()
    time.sleep(1)
    driver.find_element(By.ID, "droppableExample-tab-accept").click()
    time.sleep(1)
    ele = driver.find_element(By.ID, "notAcceptable")
    move = ActionChains(driver)
    move.click_and_hold(ele).move_by_offset(270, 0).release().perform()
    time.sleep(1)
    ele = driver.find_element(By.ID, "acceptable")
    move = ActionChains(driver)
    move.click_and_hold(ele).move_by_offset(300, 0).release().perform()
    time.sleep(1)
    driver.find_element(By.ID, "droppableExample-tab-preventPropogation").click()
    time.sleep(1)
    ele = driver.find_element(By.ID, "dragBox")
    move = ActionChains(driver)
    move.click_and_hold(ele).move_by_offset(300, 0).release().perform()
    time.sleep(1)
    move.click_and_hold(ele).move_by_offset(0, 100).release().perform()
    time.sleep(1)
    driver.execute_script("window.scrollBy(0,300)", "")
    move.click_and_hold(ele).move_by_offset(0, 300).release().perform()
    time.sleep(1)
    move.click_and_hold(ele).move_by_offset(0, -120).release().perform()
    time.sleep(1)
    driver.find_element(By.ID, "droppableExample-tab-revertable").click()
    time.sleep(1)
    ele = driver.find_element(By.ID, "revertable")
    move = ActionChains(driver)
    move.click_and_hold(ele).move_by_offset(300, 0).release().perform()
    time.sleep(1)
    ele = driver.find_element(By.ID, "notRevertable")
    move = ActionChains(driver)
    move.click_and_hold(ele).move_by_offset(300, 0).release().perform()
    time.sleep(1)


def test_draggable():
    driver.implicitly_wait(2)
    ele = driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div[1]/div/div/div[5]/div/ul/li[5]")
    driver.execute_script("arguments[0].click();", ele)
    time.sleep(1)
    driver.execute_script("window.scrollBy(0,300)", "")
    ele = driver.find_element(By.CSS_SELECTOR, "#dragBox")
    move = ActionChains(driver)
    move.click_and_hold(ele).move_by_offset(250, 40).release().perform()
    time.sleep(0.5)
    move.click_and_hold(ele).move_by_offset(110, 200).release().perform()
    time.sleep(0.5)
    move.click_and_hold(ele).move_by_offset(-60, -100).release().perform()
    time.sleep(1)
    driver.find_element(By.ID, "draggableExample-tab-axisRestriction").click()
    time.sleep(1)
    ele = driver.find_element(By.ID, "restrictedX")
    move = ActionChains(driver)
    move.click_and_hold(ele).move_by_offset(400, 100).release().perform()
    print("Only X Box works as planned.:)")
    time.sleep(1)
    ele = driver.find_element(By.ID, "restrictedY")
    move = ActionChains(driver)
    move.click_and_hold(ele).move_by_offset(-200, 300).release().perform()
    print("Only Y Box works as planned.:)")
    time.sleep(1)
    driver.find_element(By.ID, "draggableExample-tab-containerRestriction").click()
    time.sleep(1)
    ele = driver.find_element(By.CSS_SELECTOR, "#containmentWrapper > div")
    move = ActionChains(driver)
    move.click_and_hold(ele).move_by_offset(400, 300).release().perform()
    print("Success! Cannot drag small box out of the bigger box!")
    time.sleep(1)
    driver.find_element(By.ID, "draggableExample-tab-containerRestriction").click()
    time.sleep(1)
    ele = driver.find_element(By.XPATH, "//*[@id='draggableExample-tabpane-containerRestriction']/div[2]/span")
    move = ActionChains(driver)
    move.click_and_hold(ele).move_by_offset(50, -100).release().perform()
    print("Success! Cannot drag small box out of the parent!")
    time.sleep(1)
    driver.find_element(By.ID, "draggableExample-tab-cursorStyle").click()
    time.sleep(1)
    ele = driver.find_element(By.ID, "cursorCenter")
    move = ActionChains(driver)
    move.click_and_hold(ele).move_by_offset(300, 200).release().perform()
    time.sleep(1)
    ele = driver.find_element(By.ID, "cursorBottom")
    move = ActionChains(driver)
    move.click_and_hold(ele).move_by_offset(30, -200).release().perform()
    time.sleep(1)
    ele = driver.find_element(By.ID, "cursorTopLeft")
    move = ActionChains(driver)
    move.click_and_hold(ele).move_by_offset(-30, 200).release().perform()
    time.sleep(1)
    driver.quit()
