import pytest
from selenium import webdriver


@pytest.mark.optionalhook
# it is hook for delete/Modify Environment infor in HTML Report
def pytest_metadata(metadata):
    metadata.pop("Plugins", None)
    metadata.pop("Platform", None)
    metadata.pop("Python", None)
    metadata.pop("Packages", None)


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

# if you want to use incognito mode for your execution just comment out above fixture and enable below:

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
