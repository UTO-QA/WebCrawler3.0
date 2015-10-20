# imports
import sqlite3, settings
from flask import Flask, request, session, g, redirect, url_for, \
     abort, render_template, flash

settings.init()

def connect_db():
	return sqlite3.connect(settings.app.config['DATABASE'])

@settings.app.route('/')
def login_page():
	return render_template('index.html')

if __name__ == '__main__':
	settings.app.run()

