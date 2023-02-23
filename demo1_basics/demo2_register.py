import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path='C:\\Users\\112552\\Downloads\\chromedriver_win32\\chromedriver.exe')
driver.get("https://www.facebook.com/")
driver.maximize_window()
driver.implicitly_wait(30)

driver.find_element(By.LINK_TEXT, "Create new account").click()
time.sleep(5)
driver.find_element(By.NAME, "firstname").send_keys("Shefali")
#
driver.find_element(By.NAME, "lastname").send_keys("Shah")
#reg_passwd__
driver.find_element(By.ID, "password_step_input").send_keys("admin")
driver.find_element(By.ID, "password_step_input").send_keys("admin")
#driver.find_element(By.NAME, "sex")[3].click()

driver.find_element(By.NAME, "websubmit").click()