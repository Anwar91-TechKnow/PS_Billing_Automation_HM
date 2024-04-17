from selenium import webdriver
import time
import pytest
from selenium.common import TimeoutException, NoAlertPresentException, InvalidSessionIdException, NoSuchElementException
from TestCases.conftest import driver
import allure
from tkinter import simpledialog, messagebox
import tkinter as tk
from tkinter import *

from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Utilities.customlogger import LogGen
from Utilities.readproperties import TestReadConfig
from Utilities.readproperties import Test_ndepdetails
import pandas as pd
import fsspec
import openpyxl

logger = LogGen.loggenndep()
locator = Test_ndepdetails

# demo set 1
# eid1 = '12'  # InValid
# eid2 = '22'  # InValid
# eid3 = '33'  # InValid
# eid4 = '44'  # Invalid ID
# eid5 = '46'  # Invalid Id

# demo set 2 for AUS: : Make sure user having access to AUS and able to generate OTP from Google authenticator
eid1 = '1918645529217393520'  # InValid
eid2 = '1918645528447186280'  # Valid
eid3 = '1341621855514392523'  # Valid
eid4 = '726598300032440792'  # Invalid ID
eid5 = '722939193238489914'  # valid ID


# # Demo set 3 for EU1 : Make sure user having access to EU1 and able to generate OTP from Google authenticator
# eid1 = '721813295076466235'  # InValid
# eid2 = '1916956089504626103'  # Valid
# eid3 = '1918363459216557958'  # Valid
# eid4 = '726598300032440792'  # Invalid ID
# eid5 = '1916956089504626103'  # valid Id


@pytest.mark.ndep
@pytest.mark.ndepall
@allure.severity(allure.severity_level.NORMAL)
def test_NDEPLogin(driver):
    try:
        driver.get(locator.test_ndepurl())
        logger.info("****Login: URL launched successfully.--")
        driver.maximize_window()
        driver.switch_to.frame(driver.find_element(By.ID, locator.test_iframendep()))
        driver.find_element(By.NAME, locator.test_usernamefield()).send_keys(locator.test_username())
        logger.info("****Login: username entered-")
        driver.find_element(By.NAME, locator.test_passwordfield()).send_keys(locator.test_password())
        logger.info("****Login: Password entered--")
        time.sleep(2)
        driver.find_element(By.ID, locator.test_ndeplogin()).click()
        logger.info("****Login: Login button clicked.--")
        time.sleep(2)
        ROOT = tk.Tk()
        ROOT.withdraw()
        ROOT.geometry("500x200")
        ROOT.title("Authentication")
        # the input dialog
        a = simpledialog.askstring(title="Authentication", prompt="Enter 6 digit code")
        driver.find_element(By.NAME, locator.test_authentication()).send_keys(a)
        logger.info("****Login:: Took authentication code from user.--")
        time.sleep(1)
        driver.find_element(By.ID, locator.test_ndeplogin()).click()
        time.sleep(1)
        if driver.find_element(By.CLASS_NAME, locator.test_loginfailed()):
            logger.info("Login Failed")
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
        timeout = 5
        element = WebDriverWait(driver, timeout).until(
            EC.visibility_of_element_located(element_locator)
        )
        # Now you can interact with the visible element
        time.sleep(2)
        element.click()
        logger.info("Engagement: clicked to search engagement detailed option.--")
        driver.switch_to.frame(locator.test_iframendep())
        time.sleep(2)
        driver.find_element(By.ID, locator.test_engagementtextbox()).click()
        driver.find_element(By.ID, locator.test_engagementtextbox()).send_keys(eid1)
        driver.find_element(By.ID, locator.test_engagementsearchbutton()).click()
        time.sleep(2)
    try:
        alert_box = driver.find_element(By.ID, locator.test_alertbox())
        if alert_box.is_displayed():
            alert_box.click()
            driver.find_element(By.ID, locator.test_engagementtextbox()).clear()
            driver.find_element(By.ID, locator.test_engagementtextbox()).send_keys(eid2)
            driver.find_element(By.ID, locator.test_engagementsearchbutton()).click()
            time.sleep(2)
        else:
            print("Continued")
    except NoSuchElementException as c:
        print(f"Continued: {c}")
        element = driver.find_element(By.XPATH, locator.test_sumamrywindow())
        if element.is_displayed():
            screenshot_path = (
                "C://Users//anwarshaikh//PycharmProjects//PS_Billing_Automation//NDEP_Screenshots//Engagement "
                "Summary//Test_01.png")
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
        driver.find_element(By.ID, locator.test_backbutton()).click()
        driver.find_element(By.ID, locator.test_engagementtextbox()).click()
        driver.find_element(By.ID, locator.test_engagementtextbox()).send_keys(eid2)
        driver.find_element(By.ID, locator.test_engagementsearchbutton()).click()
        time.sleep(2)
    try:
        alert_box = driver.find_element(By.ID, locator.test_alertbox())
        if alert_box.is_displayed():
            alert_box.click()
            driver.find_element(By.ID, locator.test_engagementtextbox()).clear()
            driver.find_element(By.ID, locator.test_engagementtextbox()).send_keys(eid3)
            driver.find_element(By.ID, locator.test_engagementsearchbutton()).click()
            time.sleep(2)
        else:
            print("Continued")
    except NoSuchElementException as d:
        print(f"Continued: {d}")
        element = driver.find_element(By.XPATH, locator.test_sumamrywindow())
        if element.is_displayed():
            screenshot_path = (
                "C://Users//anwarshaikh//PycharmProjects//PS_Billing_Automation//NDEP_Screenshots//Engagement "
                "Summary//Test_02.png")
            element.screenshot(screenshot_path)
            messagebox.showinfo("Information", "Screenshot Saved.")
            logger.info("Engagement2: Chat summary window screenshot has been saved..--")
        else:
            driver.find_element(By.XPATH, locator.test_chatsummary()).click()
            screenshot_path = (
                "C://Users//anwarshaikh//PycharmProjects//PS_Billing_Automation//NDEP_Screenshots//Engagement "
                "Summary//Test_02.png")
            element.screenshot(screenshot_path)
            messagebox.showinfo("Information", "Screenshot Saved.")
            logger.info("Engagement2: Chat summary window screenshot has been saved..--")
        time.sleep(2)
        driver.find_element(By.ID, locator.test_backbutton()).click()
        driver.find_element(By.ID, locator.test_engagementtextbox()).click()
        driver.find_element(By.ID, locator.test_engagementtextbox()).send_keys(eid3)
        driver.find_element(By.ID, locator.test_engagementsearchbutton()).click()
        time.sleep(2)
    try:
        alert_box = driver.find_element(By.ID, locator.test_alertbox())
        if alert_box.is_displayed():
            alert_box.click()
            driver.find_element(By.ID, locator.test_engagementtextbox()).clear()
            driver.find_element(By.ID, locator.test_engagementtextbox()).send_keys(eid4)
            driver.find_element(By.ID, locator.test_engagementsearchbutton()).click()
            time.sleep(2)
        else:
            print("Continued")
    except NoSuchElementException as d:
        print(f"Continued: {d}")
        element = driver.find_element(By.XPATH, locator.test_sumamrywindow())
        if element.is_displayed():
            screenshot_path = (
                "C://Users//anwarshaikh//PycharmProjects//PS_Billing_Automation//NDEP_Screenshots//Engagement "
                "Summary//Test_03.png")
            element.screenshot(screenshot_path)
            messagebox.showinfo("Information", "Screenshot Saved.")
            logger.info("Engagement3: Chat summary window screenshot has been saved..--")
        else:
            driver.find_element(By.XPATH, locator.test_chatsummary()).click()
            screenshot_path = (
                "C://Users//anwarshaikh//PycharmProjects//PS_Billing_Automation//NDEP_Screenshots//Engagement "
                "Summary//Test_03.png")
            element.screenshot(screenshot_path)
            messagebox.showinfo("Information", "Screenshot Saved.")
            logger.info("Engagement3: Chat summary window screenshot has been saved..--")
        time.sleep(2)
        driver.find_element(By.ID, locator.test_backbutton()).click()
        driver.find_element(By.ID, locator.test_engagementtextbox()).click()
        driver.find_element(By.ID, locator.test_engagementtextbox()).send_keys(eid4)
        driver.find_element(By.ID, locator.test_engagementsearchbutton()).click()
        time.sleep(2)
    try:
        alert_box = driver.find_element(By.ID, locator.test_alertbox())
        if alert_box.is_displayed():
            alert_box.click()
            driver.find_element(By.ID, locator.test_engagementtextbox()).clear()
            driver.find_element(By.ID, locator.test_engagementtextbox()).send_keys(eid5)
            driver.find_element(By.ID, locator.test_engagementsearchbutton()).click()
            time.sleep(2)
        else:
            print("Continued")
    except NoSuchElementException as d:
        print(f"Continued: {d}")
        element = driver.find_element(By.XPATH, locator.test_sumamrywindow())
        if element.is_displayed():
            screenshot_path = (
                "C://Users//anwarshaikh//PycharmProjects//PS_Billing_Automation//NDEP_Screenshots//Engagement "
                "Summary//Test_04.png")
            element.screenshot(screenshot_path)
            messagebox.showinfo("Information", "Screenshot Saved.")
            logger.info("Engagement4: Chat summary window screenshot has been saved..--")
        else:
            driver.find_element(By.XPATH, locator.test_chatsummary()).click()
            screenshot_path = (
                "C://Users//anwarshaikh//PycharmProjects//PS_Billing_Automation//NDEP_Screenshots//Engagement "
                "Summary//Test_04.png")
            element.screenshot(screenshot_path)
            messagebox.showinfo("Information", "Screenshot Saved.")
            logger.info("Engagement4: Chat summary window screenshot has been saved..--")
            time.sleep(2)
            driver.find_element(By.ID, locator.test_backbutton()).click()
            driver.find_element(By.ID, locator.test_engagementtextbox()).click()
            driver.find_element(By.ID, locator.test_engagementtextbox()).send_keys(eid5)
            driver.find_element(By.ID, locator.test_engagementsearchbutton()).click()
            time.sleep(2)
    try:
        alert_box = driver.find_element(By.ID, locator.test_alertbox())
        if alert_box.is_displayed():
            alert_box.click()
            driver.find_element(By.ID, locator.test_engagementtextbox()).clear()
            messagebox.showinfo("Information", "You reached Max attempt, Thank you")
            time.sleep(2)
        else:
            print("Continued")
    except NoSuchElementException as d:
        print(f"Continued: {d}")
        element = driver.find_element(By.XPATH, locator.test_sumamrywindow())
        if element.is_displayed():
            screenshot_path = (
                "C://Users//anwarshaikh//PycharmProjects//PS_Billing_Automation//NDEP_Screenshots//Engagement "
                "Summary//Test_05.png")
            element.screenshot(screenshot_path)
            messagebox.showinfo("Information", "Screenshot Saved.")
            logger.info("Engagement5: Chat summary window screenshot has been saved..--")
            messagebox.showinfo("Information", "You reached Max attempt, Thank you")
        else:
            driver.find_element(By.XPATH, locator.test_chatsummary()).click()
            screenshot_path = (
                "C://Users//anwarshaikh//PycharmProjects//PS_Billing_Automation//NDEP_Screenshots//Engagement "
                "Summary//Test_05.png")
            element.screenshot(screenshot_path)
            messagebox.showinfo("Information", "Screenshot Saved.")
            logger.info("Engagement5: Chat summary window screenshot has been saved..--")
            messagebox.showinfo("Information", "You reached Max attempt, Thank you")
            time.sleep(2)
            driver.find_element(By.ID, locator.test_backbutton()).click()
            driver.switch_to.default_content()
            logger.info("NDEP Multiple Searches Completed successfully.--")
            logger.info("Testcase ended.--")
            driver.close()
