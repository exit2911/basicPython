#read text file if file mode is 'r'


fileName = input("Give us a filename: ") + ".txt" #enter the name of the file, of which we want to display its content

myFile = open(fileName,'r') #similar to VBA with current workbook. with current file -> add to it

#myFile.write(stringToSave) #write

if myFile.mode == 'r':
    contents = myFile.read()
    print(contents)
