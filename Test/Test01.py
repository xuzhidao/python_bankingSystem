import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

s = Service('/Users/zhidaoxu/Development/chromedriver')
driver = webdriver.Chrome(service=s)
driver.get("https://in.linkedin.com/")
time.sleep(3)
driver.find_element(By.LINK_TEXT,"Sign in").click()
time.sleep(3)
driver.find_element(By.PARTIAL_LINK_TEXT,"Forgot").click()
time.sleep(3)
driver.find_element(By.LINK_TEXT,"Join now").click()
time.sleep(3)
driver.find_element(By.NAME,"email-or-phone").send_keys("dummyname@abc.com")
time.sleep(3)
driver.find_element(By.ID,"password").send_keys("pwd123")
time.sleep(3)
driver.find_element(By.CLASS_NAME,"join-form__show-password-btn").click()
time.sleep(3)
driver.find_element(By.NAME, "email-or-phone").clear()
driver.find_element(By.NAME, "email-or-phone").send_keys("sam")
time.sleep(6)
driver.find_element(By.ID, "password").click()
time.sleep(6)

driver.close()
