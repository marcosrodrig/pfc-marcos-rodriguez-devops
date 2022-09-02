# https://onecore.net/selenium-webdriver-for-python.htm
import time
# import outlook
from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# driver = webdriver.Firefox()
driver = webdriver.Chrome("C:/Users/RichDotCom/Python Files/chromedriver.exe")
driver.get("http://192.168.56.103:8123")
elemento1 = driver.find_element(By.ID, "user")
elemento1.clear()
elemento1.send_keys("root")

elemento2 = driver.find_element(By.ID, "pass")
elemento2.clear()
elemento2.send_keys("password")

driver.find_element(By.XPATH, "/html/body/div/div[2]/div/form/div[3]/div/input").click()

time.sleep(10)

driver.find_element(By.XPATH, "/html/body/div/div[1]/div[6]/form[2]/div[1]/input").click()

time.sleep(10)
driver.close()


