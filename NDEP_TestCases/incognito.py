import pytest
from selenium import webdriver


# @pytest.fixture
# def driver():
#     # Create a WebDriver instance (in this case, Chrome)
#     chrome_options = webdriver.ChromeOptions()
#     chrome_options.add_argument("--incognito")
#     driver = webdriver.Chrome(options=chrome_options)
#
#     # Yield the driver instance to make it available to the test
#     yield driver
#
#     # After the test, close the browser window
#     driver.quit()