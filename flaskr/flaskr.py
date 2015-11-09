# imports
import sqlite3, settings
from variables import Globals
from ASUCrawler import Crawler
from ASUCrawler import Crawler
from flask import Flask, request, session, g, redirect, url_for, \
     abort, render_template, flash
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import os

settings.init()
global ALLOWED_EXTENSIONS
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'csv', 'xls', 'xlsx'])

def connect_db():
	return sqlite3.connect(settings.app.config['DATABASE'])

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@settings.app.route('/')
def login_page():
	return render_template('index.html')

@settings.app.route('/submit',methods=['POST'])
def formDetails():
	# perform login on ASU's website
	x = Crawler()
	# get username and password from login Form
	global username
	username = request.form['username']
	global password
	password = request.form['password']
	# website to crawl
	global website
	website = request.form['website']
	# select between myASU-Prod/QA
	option = request.form['myASU']
	file = request.files['filename']
	if file:
		filename = file.filename
		print filename
		file.save(os.path.join(settings.app.config['UPLOAD_FOLDER'], filename))
		Crawler.login(x,username,password,website,option,filename)
	else:
		Crawler.login(x,username,password,website,option,'')

if __name__ == '__main__':
	settings.app.run()

