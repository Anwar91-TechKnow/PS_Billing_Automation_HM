from selenium import webdriver
import time
import pytest
from selenium.common import NoSuchElementException, InvalidSessionIdException
from TestCases.conftest import driver
import allure
from tkinter import simpledialog, messagebox
import tkinter as tk
from tkinter import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Utilities.customlogger import LogGen
from Utilities.readproperties import TestReadConfig
from Utilities.readproperties import Test_ndepdetails

logger = LogGen.loggenndep()
locator = Test_ndepdetails


@pytest.mark.ndeplogin
@pytest.mark.ndepall
@allure.severity(allure.severity_level.NORMAL)
def test_NDEPLogin(driver):
    try:
        driver.get(locator.test_ndepurl())
        logger.info("Single_Search_test: URL launched successfully.--")
        driver.maximize_window()
        driver.switch_to.frame(driver.find_element(By.ID, locator.test_iframendep()))
        driver.find_element(By.NAME, locator.test_usernamefield()).send_keys(locator.test_username())
        logger.info("Single_Search_test: username entered-")
        driver.find_element(By.NAME, locator.test_passwordfield()).send_keys(locator.test_password())
        logger.info("Single_Search_test: Password entered--")
        time.sleep(2)
        driver.find_element(By.ID, locator.test_ndeplogin()).click()
        logger.info("Single_Search_test: Login button clicked.--")
        time.sleep(2)
        ROOT = tk.Tk()
        ROOT.withdraw()
        ROOT.geometry("500x200")
        ROOT.title("Authentication")
        # the input dialog
        a = simpledialog.askstring(title="Authentication", prompt="Enter 6 digit code")
        driver.find_element(By.NAME, locator.test_authentication()).send_keys(a)
        logger.info("Single_Search_test: Took authentication code from user.--")
        time.sleep(1)
        driver.find_element(By.ID, locator.test_ndeplogin()).click()
        time.sleep(1)
        if driver.find_element(By.CLASS_NAME, locator.test_loginfailed()):
            logger.info("Single_Search_test:Login Failed")
            messagebox.showerror("Login Failed", "Please check OTP and try again")
            driver.close()
        else:
            logger.info("Login successful.")
    except InvalidSessionIdException as e:
        print(f"Continued: {e}")
    except NoSuchElementException as b:
        print(f"Continued: {b}")
        driver.switch_to.default_content()
        element_locator = (By.LINK_TEXT, locator.test_engagementdetails())
        timeout = 10
        element = WebDriverWait(driver, timeout).until(
            EC.visibility_of_element_located(element_locator)
        )
        # Now you can interact with the visible element
        time.sleep(2)
        element.click()
        logger.info("Single_Search_test: clicked to search engagement detailed option.--")
        driver.switch_to.frame(locator.test_iframendep())
        time.sleep(2)
        ROOT = tk.Tk()
        ROOT.withdraw()
        ROOT.geometry("500x200")
        ROOT.title("Engagement")
        # the input dialog
        b = simpledialog.askstring(title="Engagement", prompt="Enter engagement ID")
        driver.find_element(By.ID, locator.test_engagementtextbox()).send_keys(b)
        logger.info("Single_Search_test: Entered the engagement ID.--")
        driver.find_element(By.ID, locator.test_engagementsearchbutton()).click()
        logger.info("Single_Search_test: clicked to search engagement detailed button.--")
        time.sleep(2)
    try:
        alert_box = driver.find_element(By.ID, locator.test_alertbox())
        if alert_box.is_displayed():
            alert_box.click()
            messagebox.showinfo("Error", "Engagement details not found.Kindly wait for sometime or provide valid "
                                         "Engagement ID.")
            driver.close()

            time.sleep(2)
        else:
            print("Continued")
    except NoSuchElementException as c:
        print(f"Continued: {c}")
        element = driver.find_element(By.XPATH, locator.test_sumamrywindow())
        if element.is_displayed():
            screenshot_path = (
                "C://Users//anwarshaikh//PycharmProjects//PS_Billing_Automation//NDEP_Screenshots//Engagement "
                "Summary//Singlendepsearch.png")
            element.screenshot(screenshot_path)
            messagebox.showinfo("Information", "Screenshot Saved.")
            logger.info("Engagement1: Chat summary window screenshot has been saved..--")
        else:
            driver.find_element(By.XPATH, locator.test_chatsummary()).click()
            screenshot_path = (
                "C://Users//anwarshaikh//PycharmProjects//PS_Billing_Automation//NDEP_Screenshots//Engagement "
                "Summary//Test_01.png")
            element.screenshot(screenshot_path)
            messagebox.showinfo("Information", "Screenshot Saved.")
            logger.info("Engagement1: Chat summary window screenshot has been saved..--")
            time.sleep(2)
            driver.switch_to.default_content()
            logger.info("NDEP Single_Search_test Completed successfully.--")
            logger.info("Testcase ended.--")
            driver.close()
