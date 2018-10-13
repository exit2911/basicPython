import os
from os import path
import shutil
from zipfile import ZipFile



if path.exists("text.txt"):
    
    src = path.realpath("text.txt")
    
    
    #make a backup copy
    
    dst = src + ".bak"
    
    #copy over the permissions, modification times, and other info
    
    shutil.copy(src,dst)
    
    #copy file and metadata
    
    shutil.copystat(src,dst)
    
    #rename a file
    
    os.rename("text.txt","newfile.txt")
    
    os.rename("newfile.txt","text.txt")
    
    
    #zip a file
    
    root_dir, tail = path.split(src)
    
    
    shutil.make_archive("archive","zip",root_dir)

with ZipFile("testzip.zip","w") as newzip: #add 2 files into a zip file
    
    newzip.write("text.txt")
    newzip.write("text.txt.bak")
