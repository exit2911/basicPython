
import os
from os import path
import datetime
from datetime import date, time, timedelta
import time



#print the name of the os

print(os.name)

#check if a file exists

print("Item exists: " + str(path.exists("text.txt")))

#check if it is a file

print("Item is a file " + str(path.isfile("text.txt")))

#check if it is a directory

print("Item is a directory: " + str(path.isdir("text.txt")))

#print file path


print("Item path: " + str(path.realpath("text.txt")))

#split file name from full path

print("item path and name: " + str(path.split(path.realpath("text.file")))) #yields a tuple of the path of the folder containing the file & the file name (path.split)


#get modification time

t = time.ctime(path.getmtime("text.txt"))

print(t)

print(datetime.datetime.fromtimestamp(path.getmtime("text.txt")))

#how long ago the item was modified

td = datetime.datetime.now() - datetime.datetime.fromtimestamp(path.getmtime("text.txt"))


print("It has been " + str(td) + " since the file was modified.")

print("Or, " + str(td.total_seconds()) + " seconds ")
