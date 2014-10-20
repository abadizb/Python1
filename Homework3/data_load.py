import os
import fnmatch
import pickle
import sys
from quotes import datalist


def get_traversal_data():
    list1 = []
    start_dir = 'C:\Users\Halim\Python34'

    for directory, folders, files in os.walk(start_dir):
            for single_file in files:
                    if (fnmatch.fnmatch(single_file, "*txt") or fnmatch.fnmatch(single_file, "*log")):
                        #print("Reading... ", single_file)
                        filepath = (os.path.join(directory, single_file))
                        f = open(filepath)
                        #print("File Content...")
                        fileData = f.read()
                        filetuple = (filepath,fileData)
                        list1.append (filetuple)
                        
    f.close()
    file1 = os.path.join (os.getcwd(), 'single_file' )                   
    pickledata = open (file1,"bw")
    pickle.dump(list1,pickledata)
    pickledata.close()
    

get_traversal_data()

