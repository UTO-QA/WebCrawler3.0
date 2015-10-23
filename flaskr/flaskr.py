# imports
import sqlite3, settings
from variables import Globals
# from ASUCrawler import Crawler
from ASUCrawler import Crawler
from flask import Flask, request, session, g, redirect, url_for, \
     abort, render_template, flash
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

settings.init()

def connect_db():
	return sqlite3.connect(settings.app.config['DATABASE'])

@settings.app.route('/')
def login_page():
	return render_template('index.html')

@settings.app.route('/submit',methods=['POST'])
def formDetails():
	# get username and password from login Form
	global username
	username = request.form['username']
	global password
	password = request.form['password']
	# website to crawl
	global website
	website = request.form['website']
	# perform login on ASU's website
	x = Crawler()
	Crawler.login(x,username,password,website)
	# ASUCrawler.test()

if __name__ == '__main__':
	settings.app.run()

