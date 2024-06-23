# open the file file2.txt in read mode
fileptr = open("file1.txt","r")
#initially the filepointer is at 0
print("The filepointer is at byte :",fileptr.tell())
#changing the file pointer location to 10.
fileptr.seek(4)
#tell() returns the location of the fileptr.
print("After reading, the filepointer is at:",fileptr.tell())
#read Content
text=fileptr.read()
print(text)
#read content
fileptr.seek(2)
text=fileptr.read()
print(text)
fileptr.close()