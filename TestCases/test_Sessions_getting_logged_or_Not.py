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


@pytest.mark.demo
@pytest.mark.all
@allure.severity(allure.severity_level.NORMAL)
def test_1(driver):
    logger.info("--TC#1 (test_Sessions_getting_logged_or_Not) Started--")
    driver.get(locator.test_getapplicationURL())  # to lunch URL
    logger.debug("--TC#1 -Launched the URL Successfully.--")
    driver.maximize_window()
    time.sleep(5)
    driver.find_element(By.ID, 'onetrust-accept-btn-handler').click()
    time.sleep(2)
    driver.find_element(By.XPATH, locator.test_chaticon()).click()
    time.sleep(2)
    driver.switch_to.frame(driver.find_element(By.NAME, locator.test_frameswitch()))
    a = driver.find_element(By.XPATH, locator.test_chattextarea())
    b = driver.find_element(By.XPATH, locator.test_sendbutton())
    a.click()
    a.send_keys(locator.test_initialmsg())  # this will give us chat information which help to get translation id
    logger.info("--TC#1 -chatinfo messages initialed, Screenshot and text of chatinfo has been collected--")
    b.click()
    time.sleep(3)
    # Below code, we are getting chat info in text format and saving at given path.
    # if you want to save file in same folder where text case is present just commented out long path
    # and remove # sign from path which has just name file.
    content = driver.find_element(By.XPATH, locator.test_chatinfo()).text
    # file_path = "Testcase#1.txt"
    # if you want to use specific path just remove
    file_path = "C://Users//anwarshaikh//PycharmProjects//PS_Billing_Automation//Chatinfo_details//TC#1_Chatinfo.text"
    # Open the file for writing
    with open(file_path, "w") as file:
        # Write the output text to the file
        file.write(content)
    time.sleep(2)

    # here we are taking screenshot of the chat-screen (iframe only) not the complete desktop window
    element = driver.find_element(By.XPATH, locator.test_chatwindow())
    allure.attach(element.screenshot_as_png, name="test_Sessions_getting_logged_or_Not",
                  attachment_type=attachment_type.PNG)
    screenshot_path = "C://Users//anwarshaikh//PycharmProjects//PS_Billing_Automation//Screenshots//TC#1_Chatinfo.png"
    element.screenshot(screenshot_path)
    time.sleep(2)

    # from below section actual text will get provide by web driver.
    # you can modify send keys text as per your choice however not recommended to use your own text
    # to just avoid code issue.

    a.send_keys("Hi, Good Morning")
    b.click()
    time.sleep(3)
    logger.info("--TC#1 -scripts are interacting with chat window and able to send messages/utterances successfully.--")
    a.send_keys("I want to know my tax information")
    b.click()
    time.sleep(3)
    a.send_keys("Could you please help me")
    b.click()
    time.sleep(3)
    a.send_keys("you contact details")
    b.click()
    time.sleep(3)
    a.send_keys("I am your customer")
    b.click()
    time.sleep(3)
    a.send_keys("where i can see you")
    b.click()
    time.sleep(3)
    a.send_keys("Hey are you there?")
    b.click()
    time.sleep(3)
    a.send_keys("What is the status of my request")
    b.click()
    time.sleep(3)
    a.send_keys("I don't have session id")
    b.click()
    time.sleep(3)
    a.send_keys("Take care bye, Have a nice day!")
    b.click()
    time.sleep(3)
    driver.find_element(By.XPATH, locator.test_closechat2()).click()
    driver.find_element(By.XPATH, locator.test_endchat2()).click()
    driver.switch_to.default_content()
    logger.info("--TC#1 -Able to close chat successfully.--")
    logger.info("--TC#1 - Test cases ended successfully--")
    driver.close()


