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
    c.execute('DELETE FROM project1_registration WHERE username = (?)',(username))
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

# Reading questions and answers of respective quiz
questions=[]
answers_choice=[]
indexes=[]
def make_list_of_q():
    cwd = os.getcwd()
    path = os.path.join(cwd,f"quiz_wise_questions")
    os.chdir(path)
    global text
    df = pd.read_csv(f"q{n}.csv")
    text = df.values.tolist()
    i=0
    for row in text:
        li=[]
        li.append(row[2])
        li.append(row[3])
        li.append(row[4])
        li.append(row[5])
        answers_choice.append(li)
        questions.append(row[1])
        indexes.append(i)
        i+=1
    os.chdir(cwd)



def startIspressed():
    print("True")
    labeltext.destroy()
    btnStart.destroy()
    make_list_of_q()
    # startquiz()

def quiz(roll,lr):
    global n,root,labeltext,btnStart
    n=input("Kindly input the quiz set you woulld like to attempt from 1-3:")
    root = tkinter.Tk()
    root.title(f"Quiz {n}")
    root.geometry("700x400")
    root.config(background="#ffffff")
    root.resizable(0,0)
    labeltext = Label(
        root,
        text = "Click start to attempt the Quiz "+n,
        font = ("Comic sans MS",24,"bold"),
        background = "#ffffff",
    )
    labeltext.pack(pady=(0,100))
    
    img2 = PhotoImage(file="Frame.png")
    btnStart = Button(
        root,
        image = img2,
        relief = FLAT,
        border = 0,
        command = startIspressed,
    )
    btnStart.pack()
    root.mainloop()
print("Kindly login to attempt the Quiz")
login()