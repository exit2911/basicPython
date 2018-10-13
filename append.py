
stringToSave = input("Give us a string : ")

fileName = input("Give us a filename: ") + ".txt"

myFile = open(fileName,'a') #similar to VBA with current workbook. with current file -> add to it

myFile.write(stringToSave) #write

myFile.close() #close
