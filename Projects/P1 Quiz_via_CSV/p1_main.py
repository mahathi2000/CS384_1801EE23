import sqlite3
import os
import csv
import re
import shutil
import pandas as pd
import hashlib
import time 
import threading
import numpy as np
import sqlite3
import os
import tkinter
from tkinter import *
os.system('cls')

# sqlite3 login and registration

with sqlite3.connect("project1_quiz_cs384.db") as db:
    cursor=db.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS project1_registration(
username VARCHAR NOT NULL,
password VARCHAR NOT NULL,
name VARCHAR NOT NULL,
whatsapp number INTEGER(10) NOT NULL
);
''')
cursor.execute('''
CREATE TABLE IF NOT EXISTS project1_marks(
roll VARCHAR NOT NULL,
quiz_num INTEGER NOT NULL,
total_marks INTEGER NOT NULL
);
''')


def registration():
    username= input('Username: ')
    password = input('Password: ')
    name = input('Name: ')
    whatsapp = input('WhatsApp Number: ')
    h = hashlib.md5(password.encode())
    db = sqlite3.connect('project1_quiz_cs384.db')
    c = db.cursor()
    c.execute("INSERT INTO project1_registration (username,password,name,whatsapp) VALUES (?,?,?,?)",(username,h.hexdigest(),name,whatsapp))
    db.commit()
    quiz(username,0)

def login():
    user = input('Username: ')
    password = input('Password: ')
    h = hashlib.md5(password.encode())
    db = sqlite3.connect('project1_quiz_cs384.db')
    c = db.cursor()
    c.execute('SELECT * FROM project1_registration WHERE username = ? AND password = ?', (user, h.hexdigest()))
    if c.fetchall():
        quiz(user,1)
    else:
        print('Login failed. Kindly register yourself by filling in the following details')
        registration()



print("Kindly login to attempt the Quiz")
login()