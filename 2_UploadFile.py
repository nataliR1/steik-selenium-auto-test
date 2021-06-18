from selenium import webdriver
import os
import time 
from selenium.webdriver.common.by import By
from urllib3.packages.six import b

try:
	link = "http://suninjuly.github.io/file_input.html"
	browser = webdriver.Chrome()
	browser.get(link)
	firstname= browser.find_element(By.XPATH, "//input[@placeholder='Enter first name']")
	firstname.send_keys("aaa")
	lastname= browser.find_element(By.XPATH,  "//input[@placeholder='Enter last name']")
	lastname.send_keys("aaa")
	email= browser.find_element(By.XPATH,  "//input[@placeholder='Enter email']")
	email.send_keys("aaa")
	element = browser.find_element(By.XPATH, "//*[@id='file']")
	
	current_dir = os.path.abspath(os.path.dirname(__file__))
	file_path = os.path.join(current_dir, 'file.txt')
	
	element.send_keys(file_path)
	button= browser.find_element(By.XPATH, "//button[@type='submit']")
	button.click()
finally:
	  time.sleep(30)
	  browser.quit()

