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

# Add first product to cart
driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()

time.sleep(2)

# Check cart badge count
cart_badge = driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text

print("Cart Count:", cart_badge)

driver.quit()