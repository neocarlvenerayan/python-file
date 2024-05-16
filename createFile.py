f=open("newCreatedFile.txt", "a")
f.write("Appending content to file")
f.close()
f=open("newCreatedFile.txt","r") #Reading the file
print(f.read()) #Prints the text file content

f=open("Deletedfile.txt","x") #Creating a file for testing deleting of file

