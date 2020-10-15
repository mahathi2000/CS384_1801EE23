import csv, os, operator, shutil

cwd=os.getcwd()
path=cwd+'/analytics'
if os.path.exists(path):
    shutil.rmtree(path)




def course():
    headers = ['id','full_name','country','email','gender','dob','blood_group','state']
    
    # Read csv and process
    current_dir = os.getcwd()
    #print(current_dir)
    #1701CB01
    #17 : year 2017.
    # 01, 11, 12, 21 : B.tech, mtech,  msc, phd.
    # CB, 
    #list_of_ids = []
    cwd=os.getcwd()
    path=os.path.join(cwd,"analytics/course")
    os.makedirs(path,exist_ok=True)
    with open('studentinfo_cs384.csv','r') as file:
        reader = csv.reader(file, delimiter=',')
        next(reader)
        for row in reader:
            #list_of_ids.append(row[0])
            if len(row[0]) != 8:
                with open( current_dir + '/analytics/course/misc.csv', 'a', newline='') as file:
                    writer = csv.writer(file)
                    file_is_empty = os.stat(current_dir + '/analytics/course/misc.csv').st_size == 0
                    if file_is_empty:
                        writer.writerow(headers)
                    writer.writerow(row)
                    
            else:
                branch = row[0][4:6].lower()
                dc = {'01':'btech','11':'mtech','12':'msc','21':'phd'}
                degree = dc[row[0][2:4]]
                year = row[0][0:2]

                path=os.getcwd()+'/analytics/course'+'/'+branch+'/'+degree
                os.makedirs(path,exist_ok=True)
                file_name=year + '_' + branch + '_' + degree + '.csv'
                with open(path +'/'+ file_name, 'a', newline='') as file:
                    writer = csv.writer(file)
                    file_is_empty = os.stat(path +'/'+ file_name).st_size == 0
                    if file_is_empty:
                        writer.writerow(headers)
                    writer.writerow(row)

    pass


def country():
    headers = ['id','full_name','country','email','gender','dob','blood_group','state']
    
    # Read csv and process
    with open('studentinfo_cs384.csv','r') as file:
        reader = csv.reader(file, delimiter=',')
        next(reader)
        for row in reader:
            country_name=row[2]
            path=os.getcwd() + '/analytics/country'
            os.makedirs(path,exist_ok=True)
            file_name = row[2]+'.csv'
            with open(path +'/'+ file_name, 'a', newline='') as file:
                writer = csv.writer(file)
                file_is_empty = os.stat(path +'/'+ file_name).st_size == 0
                if file_is_empty:
                    writer.writerow(headers)
                if len(row[0]) == 8:
                    writer.writerow(row)



    pass


def email_domain_extract():
    headers = ['id','full_name','country','email','gender','dob','blood_group','state']

    # Read csv and process
    with open('studentinfo_cs384.csv','r') as file:
        reader = csv.reader(file, delimiter=',')
        next(reader)
        for row in reader:
            email=row[3]
            path=os.getcwd()+'/analytics/email_domain'
            os.makedirs(path,exist_ok=True)
            t=0
            str=''
            for i in email:
                if i=='@':
                    t=1
                elif t==1 and i=='.':
                    break
                elif t==1:
                    str=str+i
            file_name=str+'.csv'
            with open(path +'/'+ file_name, 'a', newline='') as file:
                writer = csv.writer(file)
                file_is_empty = os.stat(path +'/'+ file_name).st_size == 0
                if file_is_empty:
                    writer.writerow(headers)
                    if len(row[0]) == 8:
                        writer.writerow(row)

    pass


def gender():
    headers = ['id','full_name','country','email','gender','dob','blood_group','state']

    # Read csv and process
    with open('studentinfo_cs384.csv','r') as file:
        reader = csv.reader(file, delimiter=',')
        next(reader)
        for row in reader:
            gen=row[4]
            path=os.getcwd() + '/analytics/gender/'
            os.makedirs(path,exist_ok=True)
            file_name = (row[4]+'.csv').lower()
            with open(path +'/'+ file_name, 'a', newline='') as file:
                writer = csv.writer(file)
                file_is_empty = os.stat(path +'/'+ file_name).st_size == 0
                if file_is_empty:
                    writer.writerow(headers)
                if len(row[0]) == 8:
                    writer.writerow(row)
              
    pass


def dob():
    headers = ['id','full_name','country','email','gender','dob','blood_group','state']
    # Read csv and process
    with open('studentinfo_cs384.csv','r') as file:
        reader = csv.reader(file, delimiter=',')
        next(reader)
        for row in reader:
            birthday=row[5]
            year=int(birthday[-4:])
            path=os.getcwd() + '/analytics/dob/'
            os.makedirs(path,exist_ok=True)
            if 1995<=year<=1999:
                file_name='bday_1995_1999.csv'
            if 2000<=year<=2004:
                file_name='bday_2000_2004.csv'
            if 2005<=year<=2009:
                file_name='bday_2005_2009.csv'
            if 2010<=year<=2014:
                file_name='bday_2010_2014.csv'
            if 2015<=year<=2020:
                file_name='bday_2015_2020.csv'
            with open(path +'/'+ file_name, 'a', newline='') as file:
                writer = csv.writer(file)
                file_is_empty = os.stat(path +'/'+ file_name).st_size == 0
                if file_is_empty:
                    writer.writerow(headers)
                if len(row[0]) == 8:
                    writer.writerow(row)    

    pass


def state():
    headers = ['id','full_name','country','email','gender','dob','blood_group','state']

    # Read csv and process
    with open('studentinfo_cs384.csv','r') as file:
        reader = csv.reader(file, delimiter=',')
        next(reader)
        for row in reader:
            stateofbirth=row[7]
            path=os.getcwd() + '/analytics/state/'
            os.makedirs(path,exist_ok=True)
            file_name = (row[7]+'.csv').lower()
            with open(path +'/'+ file_name, 'a', newline='') as file:
                writer = csv.writer(file)
                file_is_empty = os.stat(path +'/'+ file_name).st_size == 0
                if file_is_empty:
                    writer.writerow(headers)
                if len(row[0]) == 8:
                    writer.writerow(row)
    pass


def blood_group():


    pass


def new_file():

    pass


# Create the new file here and also sort it in this function only.
def new_file_sort():

    pass


