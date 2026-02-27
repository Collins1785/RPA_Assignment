from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time
import os


# -----------------------------
# Screenshot Helper
# -----------------------------
def take_screenshot(driver, name):
    folder = "screenshots"
    os.makedirs(folder, exist_ok=True)
    filepath = os.path.join(folder, f"{name}.png")
    driver.save_screenshot(filepath)
    print(f"Screenshot saved: {filepath}")


# -----------------------------
# Chrome Options (Prevents Pop-ups)
# -----------------------------
chrome_options = Options()

chrome_options.add_experimental_option("prefs", {
    "credentials_enable_service": False,
    "profile.password_manager_enabled": False
})

chrome_options.add_argument("--disable-infobars")
chrome_options.add_argument("--disable-notifications")
chrome_options.add_argument("--disable-save-password-bubble")
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--incognito")

driver = webdriver.Chrome(options=chrome_options)


# -----------------------------
# 1. Login Use Case
# -----------------------------
def login(driver):
    driver.get("https://www.saucedemo.com/")

    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "inventory_list"))
    )

    print("Login successful!")
    take_screenshot(driver, "01_login_success")


# -----------------------------
# 2. Add Items to Cart Use Case
# -----------------------------
def add_items_to_cart(driver):
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-bike-light").click()

    cart_badge = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "shopping_cart_badge"))
    )

    print("Items added to cart. Cart count:", cart_badge.text)

    take_screenshot(driver, "02_items_added")

    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    time.sleep(1)
    take_screenshot(driver, "03_cart_page")


# -----------------------------
# 3. Complete Checkout Use Case
# -----------------------------
def checkout(driver):
    driver.find_element(By.ID, "checkout").click()

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "first-name"))
    )

    driver.find_element(By.ID, "first-name").send_keys("Collins")
    driver.find_element(By.ID, "last-name").send_keys("Automation")
    driver.find_element(By.ID, "postal-code").send_keys("12345")
    driver.find_element(By.ID, "continue").click()

    take_screenshot(driver, "04_checkout_info_filled")

    driver.find_element(By.ID, "finish").click()

    success = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "complete-header"))
    )

    print("Checkout completed:", success.text)
    take_screenshot(driver, "05_order_complete")


# -----------------------------
# MAIN EXECUTION FLOW
# -----------------------------
try:
    login(driver)
    add_items_to_cart(driver)
    checkout(driver)

finally:
    time.sleep(3)
    driver.quit()