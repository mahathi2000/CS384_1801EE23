episode = int(episode)
    #         new_ep = str(episode)
    #         new_ep = new_ep.zfill(int(episode_padding))
    #         print(new_ep)

    #     #ep_name=get_ep_name(filename)
    #     match_name=re.findall(r"[a-zA-Z0-9\.\-\'\!\&\(\) ]+\.",filename)[0]
    #     name=re.split(r"\.\w",match_name)[0]
    #     #print(name)
    #     ep_name=name.split("-",2)[-1]
    #     print(ep_name)
        

    #     rename = folder_name+' - Season ' + \
    #         str(new_season)+' Episode '+str(new_ep)+' -'+str(ep_name)
    #     last = filename[-3:]
    #     # print('last:',last)
    #     if(last == 'srt'):
    #         rename = rename+'.srt'
    #     if(last == 'mp4'):
    #         rename = rename+'.mp4'

    #     os.chdir(folder_path)

    #     source_path=folder_path+filename
    #     destination_path=folder_path+rename
    #     # print(source_path)
    #     # print(destination_path)
    #     #os.rename(filename, rename)
    #     print(rename)

    # # rename Logic 