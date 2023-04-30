import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException

# Get the driver path from the CHROME_DRIVER_PATH environment variable, or use a default value
CHROMIUM_CHROME_DRIVER_URL = os.getenv('CHROME_DRIVER_PATH', '//Users/modilevskydaniel/Downloads/chromedriver_mac_arm64_m2/chromedriver')
CHROMIUM_FIREFOX_DRIVER_URL = os.getenv('FIREFOX_DRIVER_PATH', '//Users/modilevskydaniel/Downloads/chromedriver_mac_arm64_firefox/geckodriver')

browsers = {
    "chrome": "chrome",
    "firefox": "firefox",
    "safari": "safari",
    "explorer": "explorer"
}


# Function that get browser type and return webdriver.
def open_driver(browser):
    if browser == browsers['chrome']:
        driver = webdriver.Chrome(executable_path=CHROMIUM_CHROME_DRIVER_URL)
    elif browser == browsers['firefox']:
        driver = webdriver.Firefox(executable_path=CHROMIUM_FIREFOX_DRIVER_URL)
    else:
        raise ValueError("Invalid browser")
    return driver


def test_login_page():
    driver = open_driver(browsers['firefox'])
    driver.get("http://127.0.0.1:5050/login")
    driver.find_element(By.ID, "username").send_keys("admin")
    driver.find_element(By.ID, "password").send_keys("pass")
    driver.find_element(By.ID, "submit").click()

    try:
        # Wait for the dashboard page to load
        dashboard_title = WebDriverWait(driver, 10).until(
            EC.title_contains('Dashboard')
        )
        # Verify that the user is logged in
        assert dashboard_title
        assert 'dashboard' in driver.current_url.lower()
        print('Tests are successful!')

    except TimeoutException:
        # Handle the case where the dashboard page does not load in time
        print('Timed out waiting for dashboard page to load')

    finally:
        # Quit the driver to clean up the browser instance
        driver.quit()

    driver.quit()


test_login_page()
