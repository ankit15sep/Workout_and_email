import os
for dirpath, dirnames, filenames in os.walk(os.getcwd()):  
    gif_files = []
    gif_files = [gifs for gifs in filenames if gifs.endswith("gif")]
    if len(gif_files) > 0 and len(dirnames)==0:
        folder_name=os.path.basename(dirpath)
        csv_filename = folder_name+'.csv'
        csv_file = os.path.join(dirpath,csv_filename)
        exercise_list = open(csv_file,'w')
        for gif in gif_files:
            print(gif.rstrip('.gif')+', ,'+gif, file=exercise_list)
        exercise_list.close()
