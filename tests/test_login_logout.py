import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv("BASE_URL")
VALID_USERNAME = os.getenv("VALID_USERNAME")
VALID_PASSWORD = os.getenv("VALID_PASSWORD")
INVALID_USERNAME = os.getenv("INVALID_USERNAME")
INVALID_PASSWORD = os.getenv("INVALID_PASSWORD")

@pytest.fixture(scope="module")
def driver():
    options = Options()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    yield driver
    driver.quit()

def login(driver, username, password):
    driver.get(BASE_URL)
    # 1. Click login
    try:
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.NAME, "username"))
        )
    except Exception as e:
        raise e
    driver.find_element(By.NAME, "username").send_keys(username)
    driver.find_element(By.NAME, "password").send_keys(password)
    driver.find_element(By.XPATH, "//button[@type='submit']").click()

def test_valid_login(driver):
    login(driver, VALID_USERNAME, VALID_PASSWORD)
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "//span[text()='Dashboard']"))
    )
    assert "dashboard" in driver.current_url.lower()

def test_logout(driver):
    user_dropdown = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".oxd-userdropdown-name"))
    )
    user_dropdown.click()
    # 2. Click logout
    logout_btn = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//a[text()='Logout']"))
    )
    logout_btn.click()
    # 3. Verify login page is shown again
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.NAME, "username"))
    )
    time.sleep(5)
    assert BASE_URL in driver.current_url

def test_invalid_login(driver):
    # 4. check invalid login
    login(driver, INVALID_USERNAME, INVALID_PASSWORD)
    error = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "p.oxd-alert-content-text"))
    )
    time.sleep(5)
    assert error.is_displayed()






