from selenium.webdriver.common.by import By
import time
from Utilities.readproperties import TestReadConfig
import pytest
import allure
from allure import attachment_type
from Utilities.customlogger import LogGen


# to comment out a bunch of line you can use ctrl+O/ as shortcut keys
logger = LogGen.loggentestcase()
locator = TestReadConfig


@pytest.mark.smoke
@pytest.mark.all
@allure.severity(allure.severity_level.CRITICAL)
def test_5(driver):
    logger.info("--TC#5 (test_continuously_more_than_30_minutes _VA_Only) Started--")
    driver.get(locator.test_getapplicationURL())  # to lunch URL
    logger.debug("--TC#5 -Launched the URL Successfully.--")
    driver.maximize_window()
    time.sleep(5)
    driver.find_element(By.XPATH, locator.test_chaticon()).click()
    time.sleep(2)
    driver.switch_to.frame(driver.find_element(By.NAME, locator.test_frameswitch()))
    a = driver.find_element(By.XPATH, locator.test_chattextarea())
    b = driver.find_element(By.XPATH, locator.test_sendbutton())
    a.click()
    a.send_keys(locator.test_initialmsg())  # this will give us chat information which help to get translation id
    logger.info("--TC#5 -chatinfo messages initialed, Screenshot and text of chatinfo has been collected--")
    b.click()
    time.sleep(3)
    # Below code, we are getting chat info in text format and saving at given path.
    # if you want to save file in same folder where text case is present just commented out long path
    # and remove # sign from path which has just name file.
    content = driver.find_element(By.XPATH, locator.test_chatinfo()).text
    # file_path = "Testcase#1.txt"
    # if you want to use specific path just remove
    file_path = "C://Users//anwarshaikh//PycharmProjects//PS_Billing_Automation//Chatinfo_details//TC#5_Chatinfo.text"
    # Open the file for writing
    with open(file_path, "w") as file:
        # Write the output text to the file
        file.write(content)
    time.sleep(2)

    # here we are taking screenshot of the chat-screen (iframe only) not the complete desktop window
    element = driver.find_element(By.CLASS_NAME, locator.test_chatwindow())
    allure.attach(element.screenshot_as_png, name="test_continuously_more_than_30_minutes _VA_Only",
                  attachment_type=attachment_type.PNG)
    screenshot_path = "C://Users//anwarshaikh//PycharmProjects//PS_Billing_Automation//Screenshots//TC#5_Chatinfo.png"
    element.screenshot(screenshot_path)
    time.sleep(2)

    # from below section actual text will get provide by web driver.
    # you can modify send keys text as per your choice however not recommended to use your own text
    # to just avoid code issue.

    a.send_keys("Hi,Good Morning")
    logger.info("--TC#5 -scripts are interacting with chat window and able to send messages/utterances successfully.--")
    b.click()  # 2 min interval
    logger.info("--TC#5 -interval of each 2 min started.--")
    time.sleep(120)  # 1
    a.click()
    a.send_keys("I forgot my password")
    b.click()
    time.sleep(120)  # 2
    a.click()
    a.send_keys("Technical issue")
    b.click()
    time.sleep(120)  # 3
    a.click()
    a.send_keys("Secure Token having an issue")
    b.click()
    time.sleep(120)  # 4
    a.click()
    a.send_keys("Email address not working")
    b.click()
    time.sleep(120)  # 5
    a.click()
    a.send_keys("Are you there!")
    b.click()
    time.sleep(120)  # 6
    a.click()
    a.send_keys("Hey are you there?")
    b.click()
    time.sleep(120)  # 7
    a.click()
    a.send_keys("Authentication issue")
    b.click()
    time.sleep(120)  # 8
    a.click()
    a.send_keys("Error 404")
    b.click()
    time.sleep(120)  # 9
    a.click()
    a.send_keys("Username not showing")
    b.click()
    time.sleep(120)  # 10
    a.click()
    a.send_keys("Customer services")
    b.click()
    time.sleep(120)  # 11
    a.click()
    a.send_keys("subscriptions related to question")
    b.click()
    time.sleep(120)  # 12
    a.click()
    a.send_keys("Connection Lost")
    b.click()
    time.sleep(120)  # 13
    a.click()
    a.send_keys("Email address not working")
    b.click()
    time.sleep(120)  # 14
    a.click()
    a.send_keys("System error")
    b.click()
    time.sleep(120)  # 15
    a.click()
    a.send_keys("Web page is not loading")
    b.click()
    time.sleep(120)  # 16
    a.click()
    a.send_keys("Unable to see the reports")
    b.click()
    time.sleep(120)  # 17
    a.click()
    a.send_keys("Username not showing")
    b.click()
    time.sleep(2)  # 18
    logger.info("--TC#5 -36 min over.--")
    element = driver.find_element(By.CLASS_NAME, locator.test_chatwindow())
    allure.attach(element.screenshot_as_png, name="test_continuously_more_than_30_minutes _VA_Only@36min",
                  attachment_type=attachment_type.PNG)
    screenshot_path = ("C://Users//anwarshaikh//PycharmProjects//PS_Billing_Automation//Screenshots//TC"
                       "#5_36min_continue.png")
    element.screenshot(screenshot_path)
    time.sleep(2)
    a.send_keys("Goodbye")
    logger.info("--TC#5 -37 min over.--")
    b.click()
    logger.info("--TC#5 -able to continue chat for more than 30 min successfully--")
    # --------------------------------------------------
    # if you require email chat transcripts just remove comments from below code.
    # remember to update xpath or other locators in respective field.
    # -------------------------------------------------
    driver.switch_to.default_content()
    driver.switch_to.frame(driver.find_element(By.ID, 'inqChatStage'))
    driver.find_element(By.XPATH, locator.test_email()).click()
    time.sleep(2)
    driver.find_element(By.ID, locator.test_emailtextarea()).send_keys(locator.test_emailaddress())
    time.sleep(2)
    driver.find_element(By.XPATH, locator.test_emailsend()).click()
    time.sleep(2)
    driver.find_element(By.XPATH, locator.test_closechat()).click()
    driver.switch_to.default_content()
    logger.info("--TC#5 -Email transcription test case completed--")
    logger.info("--TC#5 - Test cases ended successfully--")
    driver.close()
