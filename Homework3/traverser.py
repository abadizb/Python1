import os
import fnmatch
import fnmatch
import pickle
import sys


def traverser():
    list1 = []
    start_dir = '/Users/osama/fortune1'

    for directory, folders, files in os.walk(start_dir):
            for single_file in files:
                    if (fnmatch.fnmatch(single_file, "*txt")):
                            #print("Reading... ", single_file)
                            filepath = (os.path.join(directory, single_file))
                            f = open(filepath)
                            #print("File Content...")
                            fileData = f.read()
                            filetuple = (filepath,fileData)
                            list1.append (filetuple)
                            f.close()
    pickledata = open ("raw_data.txt","bw")
    pickle.dump(list1,pickledata)
    pickledata.close()
    

traverser()
