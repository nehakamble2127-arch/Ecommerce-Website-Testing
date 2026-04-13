from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)

# Open website
driver.get("https://www.saucedemo.com/")

# Login
wait.until(EC.presence_of_element_located((By.ID, "user-name"))).send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()

# Add product to cart
wait.until(EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-backpack"))).click()

# Wait for Remove button and click it
wait.until(EC.element_to_be_clickable((By.ID, "remove-sauce-labs-backpack"))).click()

# Verify cart is empty
cart_items = driver.find_elements(By.CLASS_NAME, "shopping_cart_badge")

if len(cart_items) == 0:
    print("Product removed successfully. Cart is empty.")
else:
    print("Product still exists in cart.")

driver.quit()