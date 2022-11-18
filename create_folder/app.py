import os 
import time 

def create_folder(BASE_DIR): 
    # this function will create a folder : 
    for i in range(10): 
        os.mkdir(BASE_DIR + str(i) + 'minhaz_folder')
def create_file(BASE_DTR): 
     # this make a file : 
     for i in  range(10): 
         f= open(BASE_DTR , str(i) , 'minhaz.txt' , 'w')
         f.close()
def ranameFile(BASE_DIR) :
    # THIS FUNTION WILL RENAME THE FILE : 
    os.chdir(BASE_DIR)
    for i in os.listdir():
        filename, fileext=  os.path.splitext(i)
        print(filename,  fileext )
        os.rename(i,  i.replace('Folder', 'minhaz_folder'))
if __name__== '__main__' : 
    BASE_DIR=   'D:\python\project\create_folder'
    create_folder(BASE_DIR)
    create_file(BASE_DIR)
    time.sleep(10)
    ranameFile(BASE_DIR )
    