import settings
from variables import Globals
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import time

class Crawler:
	def login(self,username,password,website):
		import re
		# get request to MyASU login portal
		Globals.driver.get("https://webapp4.asu.edu/myasu/")
		try:
			# wait for sign-in button
			signIn = WebDriverWait(Globals.driver,20).until(
				EC.presence_of_element_located((By.ID,"login_submit"))
				)
			# grab username and password elements
			user = Globals.driver.find_element_by_id("username")
			passW = Globals.driver.find_element_by_id("password")
			# attempt login to myASU
			user.send_keys(username)
			passW.send_keys(password)
			Globals.driver.find_element_by_class_name("submit").click()
			WebDriverWait(Globals.driver,20).until(
				EC.presence_of_element_located((By.ID,"asu_footer"))
				)
		except TimeoutException:
			print "Exception!"
			Globals.driver.back()
			Globals.driver.back()
		finally:
			src = Globals.driver.page_source
			loggedIn = 'My ASU'
			isSignedIn = loggedIn in src
			if isSignedIn:
				print "You're good!"
				Globals.driver.get(website)
			else:
				print "Try again"

