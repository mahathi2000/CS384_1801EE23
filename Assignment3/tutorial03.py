import csv, os, operator, shutil





def course():
    headers = ['id','full_name','country','email','gender','dob','blood_group','state']
    cwd=os.getcwd()
    path=cwd+'/analytics'
    if os.path.exists(path):
        shutil.rmtree(path)
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


    pass


def email_domain_extract():

    pass


def gender():
              
    pass


def dob():

    pass


def state():

    pass


def blood_group():


    pass


def new_file():

    pass


# Create the new file here and also sort it in this function only.
def new_file_sort():

    pass
