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

def make_overall():
    all_grades_df=pd.read_csv('acad_res_stud_grades.csv')
    roll_grouped=all_grades_df.groupby('roll')
    for roll,group in roll_grouped:
        df_overall=pd.DataFrame(columns=['Semester','Semester Credits','Semester Credits Cleared','SPI','Total Credits','Total Credits Cleared','CPI'])
        cum_cleared=0
        credits_per_sem=[]
        spi_per_sem=[]
        sem_grouped=group.groupby('sem')
        for sem,sem_group in sem_grouped:
            try:
                #c is a list of credits of all courses of that semester of that roll
                c=sem_group['total_credits']
                #g is a list of credits obtained by that roll in that sem for various courses
                sem_group['num_credits_obtained']=sem_group['credit_obtained'].apply(grading_function)
                g = sem_group['num_credits_obtained']
                total_credits = sem_group['total_credits'].sum()
                credits_cleared = g.apply(lambda v:passed(v))
                #credits_cleared = sem_group['num_credits_obtained'].sum()

                credits_per_sem.append(sum(sem_group['total_credits']) )

                spi_numerator = np.multiply(c,g).sum()
                spi_denominator = c.sum()
                spi = spi_numerator/spi_denominator

                spi_per_sem.append(spi)


                cpi_numerator = sum(np.multiply(spi_per_sem,credits_per_sem))
                cpi_denominator = sum(credits_per_sem)

                cpi = cpi_numerator/cpi_denominator

                sem_cleared = sum(np.multiply(c,credits_cleared))

                cum_cleared += sem_cleared
                row=[sem,total_credits,sem_cleared,spi,cpi_denominator,cum_cleared,cpi]
                overall_len=len(df_overall)             
                df_overall.loc[overall_len] = row

            except:
                
                sem_len=len(sem_group)
                for i in range(sem_len):
                    misc_length=len(misc)
                    misc.loc[misc_length]=[sem_group['roll'].iloc[i],sem_group['sem'].iloc[i],sem_group['year'].iloc[i],sem_group['sub_code'].iloc[i],sem_group['total_credits'].iloc[i],sem_group['credit_obtained'].iloc[i],sem_group['sub_type'].iloc[i]]
        file_name=roll+'_'+'overall.csv'
        file_path=os.path.join(path,file_name)
        df_overall.to_csv(file_path)
    file_name='misc.csv'
    file_path=os.path.join(path,file_name)
    misc.to_csv(file_path)








make_grade_folder()
rollno_individual()
make_overall()
