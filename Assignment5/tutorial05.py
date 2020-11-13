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


parent_dir=os.getcwd()
path=os.path.join(parent_dir,"Subtitles")

def stripEp(target):
    target = target.strip()
    target = target.strip('Eabcdefghijklmnopqrstuvwxyz. ')
    return target






def rename_FIR(folder_name):
    print("Enter season padding:")
    season_padding = input()
    print("Enter episode padding:")
    episode_padding = input()
    folder_path = os.path.join(path, folder_name)
    for filename in os.listdir(folder_path):
        # season=get_season(filename)
        print(filename)
        matches = re.findall(r"Episode \d*", filename)
        
        if len(matches) == 1:
            episode = matches[0]
            episode = stripEp(episode)
            episode = int(episode)
            new_ep = str(episode)
            new_ep = new_ep.zfill(int(episode_padding))
            #print(new_ep)

        #ep_name=get_ep_name(filename)
        match_name=re.findall(r"[a-zA-Z0-9\.\-\'\!\&\(\) ]+\.",filename)[0]
        name=re.split(r"\.\w",match_name)[0]
        #print(name)
        ep_name=name.split("-",2)[-1]
        #print(ep_name)
        

        rename = folder_name+' - ' +'Episode '+str(new_ep)+' -'+ep_name

        last = filename[-3:]
        if(last == 'srt'):
            rename = rename+'.srt'
        if(last == 'mp4'):
            rename = rename+'.mp4'

        os.chdir(folder_path)

        source_path=folder_path+filename
        destination_path=folder_path+rename
        # print(source_path)
        # print(destination_path)
        #os.rename(filename, rename)
        print(rename)

    # rename Logic 
    pass
    

def rename_Game_of_Thrones(folder_name):
    print("Enter season padding:")
    season_padding = input()
    print("Enter episode padding:")
    episode_padding = input()
    folder_path = os.path.join(path, folder_name)
    for filename in os.listdir(folder_path):
        # season=get_season(filename)
        print(filename)
        matches = re.findall(r"- \d", filename)
        if len(matches) == 1:
            season = int(matches[0][2])
            new_season = str(season)
            new_season = new_season.zfill(int(season_padding))
            # print(new_season)
            # print(type(season))

        # ep=get_ep(filename)
        matches = re.findall(r"x[0-9][0-9]", filename)

        if len(matches) == 1:
            episode = matches[0]
            episode = stripEp(episode)
            episode = int(episode)
            new_ep = str(episode)
            new_ep = new_ep.zfill(int(episode_padding))
            # print(new_ep)

        # ep_name=get_ep_name(filename)
        matches = re.findall(r"- [A-Za-z_ ]*.", filename)
        if len(matches) == 2:
            # ind 1 because - 1 also matches with the reg expre
            ep_name = matches[1]
            ep_name = ep_name[2:len(ep_name)-1]

        rename = folder_name+' - Season ' + \
            str(new_season)+' Episode '+str(new_ep)+' - '+str(ep_name)
        last = filename[-3:]
        # print('last:',last)
        if(last == 'srt'):
            rename = rename+'.srt'
        if(last == 'mp4'):
            rename = rename+'.mp4'

        os.chdir(folder_path)

        # source_path=folder_path+filename
        # destination_path=folder_path+rename
        # print(source_path)
        # print(destination_path)
        os.rename(filename, rename)
        print(rename)

    pass
    # rename Logic 
    

def rename_Sherlock(folder_name):
    print("Enter season padding:")
    season_padding = input()
    print("Enter episode padding:")
    episode_padding = input()
    folder_path = os.path.join(path, folder_name)
    for filename in os.listdir(folder_path):
        # season=get_season(filename)
        print(filename)
        matches = re.findall(r"S[0-9][0-9]", filename)
        if len(matches) == 1:
            season = int(matches[0][1:])
            new_season = str(season)
            new_season = new_season.zfill(int(season_padding))
            # print(new_season)
            # print(type(season))

        # # ep=get_ep(filename)
        matches = re.findall(r"E[0-9][0-9]", filename)

        if len(matches) == 1:
            episode = matches[0][1:]
            #episode = stripEp(episode)
            episode = int(episode)
            new_ep = str(episode)
            new_ep = new_ep.zfill(int(episode_padding))
            #print(new_ep)

        

        rename = folder_name+' - Season ' + str(new_season)+' Episode '+str(new_ep)
        last = filename[-3:]
        # print('last:',last)
        if(last == 'srt'):
            rename = rename+'.srt'
        if(last == 'mp4'):
            rename = rename+'.mp4'

        os.chdir(folder_path)

        source_path=folder_path+filename
        destination_path=folder_path+rename
        #print(source_path)
        #print(destination_path)
        os.rename(filename, rename)
        print(rename)
        
    


    # rename Logic 
    pass
    

def rename_Suits(folder_name):
    print("Enter season padding:")
    season_padding = input()
    print("Enter episode padding:")
    episode_padding = input()
    folder_path = os.path.join(path, folder_name)
    for filename in os.listdir(folder_path):
        # season=get_season(filename)
        print(filename)
        matches = re.findall(r"- \d", filename)
        if len(matches) == 1:
            season = int(matches[0][2])
            new_season = str(season)
            new_season = new_season.zfill(int(season_padding))
            #print(new_season)
            # print(type(season))

        # ep=get_ep(filename)
        matches = re.findall(r"x[0-9][0-9]", filename)

        if len(matches) == 1:
            episode = matches[0]
            episode = stripEp(episode)
            episode = int(episode)
            new_ep = str(episode)
            new_ep = new_ep.zfill(int(episode_padding))
            #print(new_ep)

        #ep_name=get_ep_name(filename)
        match_name=re.findall(r"[a-zA-Z0-9\.\-\'\!\&\(\) ]+\.",filename)[0]
        name=re.split(r"\.\w",match_name)[0]
        #print(name)
        ep_name=name.split("-",2)[-1]
        #print(ep_name)
        

        rename = folder_name+' - Season ' + \
            str(new_season)+' Episode '+str(new_ep)+' -'+str(ep_name)
        last = filename[-3:]
        # print('last:',last)
        if(last == 'srt'):
            rename = rename+'.srt'
        if(last == 'mp4'):
            rename = rename+'.mp4'

        os.chdir(folder_path)

        source_path=folder_path+filename
        destination_path=folder_path+rename
        # print(source_path)
        # print(destination_path)
        os.rename(filename, rename)
        print(rename)

    pass




    # rename Logic 

    

def rename_How_I_Met_Your_Mother(folder_name):

    
    

    print("Enter season padding:")
    season_padding = input()
    print("Enter episode padding:")
    episode_padding = input()
    folder_path = os.path.join(path, folder_name)

    for filename in os.listdir(folder_path):
        # season=get_season(filename)
        print(filename) 
        matches = re.findall(r"- \d",filename)
        if len(matches)==1:
            season=int(matches[0][2])
            new_season=str(season)
            new_season=new_season.zfill(int(season_padding))
            #print(new_season)
  
        matches = re.findall(r"x[0-9][0-9]", filename)
        if len(matches) == 1:
            episode = matches[0]
            episode = stripEp(episode)
            episode=int(episode)
            new_ep=str(episode)
            new_ep=new_ep.zfill(int(episode_padding))
            #print(new_ep)
        
        matches = re.findall(r"- [a-zA-Z0-9_() ]*\.", filename)
        if len(matches) == 1:
            
            ep_name = matches[0]
            ep_name = ep_name[2:len(ep_name)-1]
            #print(ep_name)

        rename = folder_name+' - Season ' + str(new_season)+' Episode '+str(new_ep)+' - '+str(ep_name)
        last = filename[-3:]
        # print('last:',last)
        if(last == 'srt'):
            rename = rename+'.srt'
        if(last == 'mp4'):
            rename = rename+'.mp4'

        os.chdir(folder_path)

        source_path=folder_path+filename
        destination_path=folder_path+rename
        #print(source_path)
        #print(destination_path)
        try:
            os.rename(filename, rename)
            print(rename)
        except:
            os.remove(filename)


    # rename Logic 
    pass
    



print("Enter Show name:")
show_name=input()

if(show_name=='FIR'):
    rename_FIR(show_name)

if(show_name=='Game of Thrones'):
    rename_Game_of_Thrones(show_name)

if(show_name=='How I Met Your Mother'):
    rename_How_I_Met_Your_Mother(show_name)

if(show_name=='Sherlock'):
    rename_Sherlock(show_name)

if(show_name=='Suits'):
    rename_Suits(show_name)
