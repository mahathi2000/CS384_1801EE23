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

def make_groups(filename,number_of_groups,batch_strength):

    headers=['Roll','Name','Email']
    
    directory = "groups"
    # Parent Directory path
    parent_dir = os.getcwd()

    # Path
    path = os.path.join(parent_dir, directory)
    if os.path.exists(path):
        shutil.rmtree(path)
    os.mkdir(path)

    #creating empty group files
    for i in range(int(number_of_groups)):
        group_number=i+1
        padded_group= str(group_number).zfill(2)
        group_file_name='Group_G'+padded_group+'.csv'
        with open(path +'/'+ group_file_name, 'a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(headers)

    with open('branch_strength.csv','r') as file:
        reader=csv.reader(file,delimiter=',')
        next(reader)

        for row in reader:
            #print(row)
            branch_strength=int(row[1])
            #print(branch_strength)
            branch_code=row[0]
            #print(branch_code)
            csv_name=branch_code+'.csv'
            df=pd.read_csv(csv_name)
            #print(df)
            x=math.floor(int(branch_strength)/int(number_of_groups))
            start=0
            end=start+x
            
            
            
            for i in range(number_of_groups):
                group_num=i+1
                padded_group= str(group_num).zfill(2)
                group_file_name='Group_G'+padded_group+'.csv'
                #print(group_file_name)
                with open(path+'/'+group_file_name,'a',newline='') as file:
                    for j in range(start,end):
                        writer=csv.writer(file)
                        
                        row=list(df.iloc[j])
                        #print(row)
                        writer.writerow(row)
                    
                        
                start=end
                end=start+x
                padded_group= str(group_num).zfill(2)

    #code for the left over students
    with open('branch_strength.csv','r') as file:
        reader=csv.reader(file,delimiter=',')
        next(reader)
        p=0
        for row in reader:

            branch_strength=int(row[1])
            #print(branch_strength)
            branch_code=row[0]
            x=math.floor(int(branch_strength)/int(number_of_groups))
            left=branch_strength-(number_of_groups*x)
            print(left)
            start_index=branch_strength-left

            csv_name=branch_code+'.csv'
            df=pd.read_csv(csv_name)

            for i in range(start_index,branch_strength):
                group_number=p%12+1
                padded_group= str(group_number).zfill(2)
                group_file_name='Group_G'+padded_group+'.csv'
                print(group_file_name)
                with open(path+'/'+group_file_name,'a',newline='') as file:
                    writer=csv.writer(file)
                    row=list(df.iloc[i])
                    writer.writerow(row)
                    print(row)
                print(p)
                p=p+1



                        

    #make_stats_grouping(number_of_groups)

            

            # with open(csv_name,'r') as file: 
            #     reader = csv.reader(file, delimiter=',')
            #     next(reader)
            #     for row in reader:

            #     for i in range[start:end]:
            #         with open(path +'/'+ csv_name, 'a', newline='') as file:
            #         writer = csv.writer(file)
            #         writer.writerow(row)

    pass

def make_stats_grouping(number_of_groups):
    directory = "groups"
    # Parent Directory path
    parent_dir = os.getcwd()

    # Path
    path = os.path.join(parent_dir, directory)
    os.chdir(path)
    stats_file_name='stats_grouping.csv'
    header=['group','total','EE','ME','CS','CE','CB','MM']
    with open(stats_file_name, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(header)

        for i in range(number_of_groups):
            #print('This loop runs {} times',i)
            group_num=i+1
            padded_group= str(group_num).zfill(2)
            group_file_name='Group_G'+padded_group+'.csv'
            #print(group_file_name)

            #total number of stuents in this group
            with open(group_file_name,'r') as file:
                reader = csv.reader(file, delimiter=',')
                next(reader)
                lines=len(list(reader))
                #print(lines)


            all_rolls=pd.read_csv(group_file_name)
            branch_code=[]
            with open(group_file_name,'r') as file:
                reader = csv.reader(file, delimiter=',')
                next(reader)
                for row in reader:
                    roll=row[0]
                    branch=roll[4:6]
                    branch_code.append(branch)
            #print(branch_code)
            #print(len(branch_code))
            #print(all_rolls)
            #print(len(all_rolls))
            all_rolls['BRANCH_CODE']=branch_code

            #print(all_rolls)
            #df=all_rolls
            #print(df)
            #print('This group ends here')
            new_df=all_rolls.groupby(['BRANCH_CODE']).size()
            EE_count=new_df['EE']
            ME_count=new_df['ME']
            CS_count=new_df['CS']
            CE_count=new_df['CE']
            CB_count=new_df['CB']
            MM_count=new_df['MM']
            
            row=[group_file_name,lines,EE_count,ME_count,CS_count,CE_count,CB_count,MM_count]
            writer.writerow(row)
    pass
    



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
    #print(batch_strength)

    make_branch_strength(filename)
    
    make_individual_branch(filename)
    make_groups(filename,number_of_groups,batch_strength)
    make_stats_grouping(number_of_groups)




    pass









filename = "Btech_2020_master_data.csv"
number_of_groups=12

group_allocation(filename, number_of_groups)