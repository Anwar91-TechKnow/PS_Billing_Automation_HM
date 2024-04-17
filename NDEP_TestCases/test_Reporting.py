import time
import pytest
from selenium.common import InvalidSessionIdException, NoSuchElementException, TimeoutException
from selenium.webdriver import ActionChains, Keys
from TestCases.conftest import driver
import allure
from tkinter import simpledialog, messagebox
import tkinter as tk
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Utilities.customlogger import LogGen
from Utilities.readproperties import Test_ndepdetails

logger = LogGen.loggenndep()
locator = Test_ndepdetails


@pytest.mark.ndepreport
@pytest.mark.ndepall
@allure.severity(allure.severity_level.NORMAL)
def test_reporting(driver):
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
        time.sleep(3)
        # driver.find_element(By.XPATH,locator.test_projectselect()).click()
        # time.sleep(2)
        # driver.find_element(By.XPATH, locator.test_projectselect()).send_keys(locator.test_projectname())
        # time.sleep(2)
        # dropdown = driver.find_element(By.XPATH,locator.test_projectlist())
        # dropdown.send_keys(Keys.ARROW_DOWN)
        # dropdown.send_keys(Keys.ENTER)
        time.sleep(2)
        driver.find_element(By.LINK_TEXT, locator.test_reporting()).click()
        time.sleep(2)
        driver.switch_to.frame(locator.test_iframendep())
        time.sleep(4)
        driver.find_element(By.XPATH, locator.test_ActiveReports()).click()
        time.sleep(2)
        element_to_hover_over = driver.find_element(By.ID, locator.test_standradreport())
        time.sleep(3)
        actions = ActionChains(driver)
        actions.move_to_element(element_to_hover_over)
        actions.perform()
        time.sleep(2)
        wait = WebDriverWait(driver, 10)
        dropdown_menu1 = wait.until(EC.visibility_of_element_located((By.ID, locator.test_vareport())))
        actions = ActionChains(driver)
        actions.move_to_element(dropdown_menu1)
        actions.perform()
        time.sleep(2)
        driver.find_element(By.ID,locator.test_billablevareport()).click()
        time.sleep(2)
        driver.find_element(By.XPATH, locator.test_daterangereport()).click()
        time.sleep(3)
        summary = driver.find_element(By.XPATH, locator.test_reportcountwindow())
        screenshot_path = (
            "C://Users//anwarshaikh//PycharmProjects//PS_Billing_Automation//NDEP_Screenshots//Reporting Validations//Reporting_Summary.png")
        summary.screenshot(screenshot_path)
        messagebox.showinfo("Information", "VA Report Screenshot saved")
        time.sleep(2)
        driver.close()
