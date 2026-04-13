from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

# Open website
driver.get("https://www.saucedemo.com/")

# Login
driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()

time.sleep(2)

# Add product to cart
driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()

time.sleep(1)

# Open cart
driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

time.sleep(1)

# Click checkout
driver.find_element(By.ID, "checkout").click()

time.sleep(1)

# Enter customer info
driver.find_element(By.ID, "first-name").send_keys("Neha")
driver.find_element(By.ID, "last-name").send_keys("Kamble")
driver.find_element(By.ID, "postal-code").send_keys("400001")

# Continue
driver.find_element(By.ID, "continue").click()

time.sleep(1)

# Finish order
driver.find_element(By.ID, "finish").click()

time.sleep(2)

# Verify success message
success_message = driver.find_element(By.CLASS_NAME, "complete-header").text

print("Order Status:", success_message)

driver.quit()