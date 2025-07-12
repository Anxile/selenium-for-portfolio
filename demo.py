from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Edge()
driver.maximize_window()

driver.get("https://www.bytecho.ca/")
print("current path:",driver.current_url)


login_button = driver.find_element(By.ID,"login")
login_button.click()

print("Title:",driver.title)
print("current path:",driver.current_url)

user_name = driver.find_element(By.ID, "user_name")
user_pass = driver.find_element(By.ID, "user_password")

user_name.send_keys("Yihe_mac")
user_pass.send_keys("12356")


driver.find_element(By.NAME,"commit").click()

success_url = "https://www.bytecho.ca/posts"
print("status:", success_url == driver.current_url)

sleep(5)
driver.quit()