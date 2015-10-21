from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class Crawler:
	global driver
	driver = webdriver.Firefox();
	def login(self,username,password):
		# get request to MyASU login portal
		driver.get("https://webapp4.asu.edu/myasu/")
		try:
			# wait for sign-in button
			signIn = WebDriverWait(driver,20).until(
				EC.presence_of_element_located((By.ID,"login_submit"))
				)
			# grab username and password elements
			user = driver.find_element_by_id("username")
			passW = driver.find_element_by_id("password")
			# attempt login to myASU
			user.send_keys(username)
			passW.send_keys(password)
			driver.find_element_by_class_name("submit").click()
			WebDriverWait(driver,20).until(
				EC.presence_of_element_located((By.ID,"asu_footer"))
				)
		finally:
			driver.quit()
