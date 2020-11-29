import os
import re
import csv
import operator
import shutil
import pandas as pd
import numpy as np
import math
import hashlib

os.system("cls")

def make_individual_branch(filename):
    path=os.getcwd()
    all_rolls=pd.read_csv(filename)
    branch_code=[]
    with open(filename,'r') as file:
        reader = csv.reader(file, delimiter=',')
        next(reader)
        for row in reader:
            roll=row[0]
            branch=roll[4:6]
            branch_code.append(branch)
        
        all_rolls['BRANCH_CODE']=branch_code

        #print(all_rolls)
    df=all_rolls
    branch_grouped= df.groupby('BRANCH_CODE')
    for branch,group in branch_grouped:
        branch_csv_name=branch+'.csv'


        branch_df=pd.DataFrame(columns=['Roll','Name','Email'])
        
        branch_df['Roll']=group['Roll']
        branch_df['Name']=group['Name']
        branch_df['Email']=group['Email']

        file_path=os.path.join(path,branch_csv_name)
        branch_df.to_csv(file_path,header=True,index=False)

        

        


    pass





def make_branch_strength(filename):
    all_rolls=pd.read_csv(filename)
    branch_code=[]
    with open(filename,'r') as file:
        reader = csv.reader(file, delimiter=',')
        next(reader)
        for row in reader:
            roll=row[0]
            branch=roll[4:6]
            branch_code.append(branch)
        
        all_rolls['BRANCH_CODE']=branch_code

        #print(all_rolls)
    df=all_rolls

    new_df=df.groupby(['BRANCH_CODE']).size()
    file_name='branch_strength.csv'
    path=os.getcwd()
    # directory = "groups"
    # # Parent Directory path 
    # parent_dir = os.getcwd()
    
    # # Path 
    # path = os.path.join(parent_dir, directory)
    # os.mkdir(path)



    file_path=os.path.join(path,file_name)
    new_df.to_csv(file_path,header=True,index=True)
    df=pd.read_csv(file_name)
    #adding header to the dataframe
    df.columns = ['BRANCH_CODE','STRENGTH']
    #sorting the dataframe wrt STRENGTH
    new_df=df.sort_values(by=['STRENGTH'],ascending=False)
    #converting the df to csv
    new_df.to_csv(file_path,header=True,index=False)



    pass 







def group_allocation(filename, number_of_groups):
    # Entire Logic 
	# You can add more functions, but in the test case, we will only call the group_allocation() method,

    # cwd=os.getcwd()
    # path=cwd+'/groups'
    # if os.path.exists(path):
    #     shutil.rmtree(path)

    # directory = "groups"
    # # Parent Directory path 
    # parent_dir = os.getcwd()
    
    # # Path 
    # path = os.path.join(parent_dir, directory) 
    
 
    # os.mkdir(path) 

    file = open(filename)
    
    reader = csv.reader(file)
    batch_strength= len(list(reader))-1
    print(batch_strength)

    #make_branch_strength(filename)
    make_individual_branch(filename)




    pass









filename = "Btech_2020_master_data.csv"
number_of_groups=input()

group_allocation(filename, number_of_groups)