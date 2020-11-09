import csv
import operator
import shutil
import os
import pandas as pd
import numpy as np
import math

os.system("cls")




grade_numeric = {
    'AA': 10,
    'AB': 9,
    'BB': 8,
    'BC': 7,
    'CC': 6,
    'CD': 5,
    'DD': 4,
    'F': 0,
    'I': 0
}


def grading_function(x):
    return grade_numeric.get(x)


def passed(v):
    if v > 0:
        return 1
    else:
        return 0


def make_grade_folder():
    cwd = os.getcwd()
    path = cwd+'/grades'
    if os.path.exists(path):
        shutil.rmtree(path)

    directory = "grades"
    # Parent Directory path
    parent_dir = os.getcwd()

    # Path
    path = os.path.join(parent_dir, directory)
    os.mkdir(path)
    pass


misc = pd.DataFrame(columns=['roll','sem','year','sub_code','total_credits','credit_obtained','sub_type'])

directory = "grades"
# Parent Directory path
parent_dir = os.getcwd()

# Path
path = os.path.join(parent_dir, directory)


def rollno_individual():
    headers = ['Subject', 'Credits', 'Type', 'Grade', 'Sem']
    with open('acad_res_stud_grades.csv', 'r') as file:
        reader = csv.reader(file, delimiter=',')
        next(reader)
        path = os.getcwd() + '/grades'
        for row in reader:
            if row[4]=='' or row[5]=='' or row[8]=='' or row[6]=='' or row[2]=='':
                continue
            file_name = row[1]+'_'+'individual'+'.csv'
            with open(path + '/' + file_name, 'a', newline='') as file:
                writer = csv.writer(file)
                file_is_empty = os.stat(path + '/' + file_name).st_size == 0
                if file_is_empty:
                    #Roll: row[1]
                    # Semester Wise Details
                    writer.writerow(headers)

                # sub,credit,type,grade,sem
                

                thisrow = [row[4], row[5], row[8], row[6], row[2]]
                writer.writerow(thisrow)
    pass











make_grade_folder()
rollno_individual()
#make_overall()
