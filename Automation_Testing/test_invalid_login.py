from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

# Open website
driver.get("https://www.saucedemo.com/")

# Enter wrong login credentials
driver.find_element(By.ID, "user-name").send_keys("wrong_user")
driver.find_element(By.ID, "password").send_keys("wrong_password")

# Click login
driver.find_element(By.ID, "login-button").click()

time.sleep(2)

# Capture error message
error_message = driver.find_element(By.CLASS_NAME, "error-message-container").text

print("Error Message:", error_message)

driver.quit()