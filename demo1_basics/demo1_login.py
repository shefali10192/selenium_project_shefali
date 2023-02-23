import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path='C:\\Users\\112552\\Downloads\\chromedriver_win32\\chromedriver.exe')
driver.get("https://www.facebook.com/")
print(driver.title)
time.sleep(5)

driver.find_element(By.ID, "email").send_keys("shefali10192@gmail.com")
driver.find_element(By.ID, "pass").send_keys("Shefali1010@")
driver.find_element(By.NAME, "login").click()

driver.quit()
