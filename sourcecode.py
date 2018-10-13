

import os

stringToSave = input("Give us a string : ")

fileName = input("Give us a filename: ") + ".txt"

myFile = open(fileName,'w') #similar to VBA with current workbook. with current file -> write

myFile.write(stringToSave) #write

myFile.close() #close
