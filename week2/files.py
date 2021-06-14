#f = open("C:\learn-automation\learn-python-kirk\week2\show_version.txt")
#print(f)
#print(f.read())
#print(f.splitlines())>>Does not exist
#output=f.readlines()>> does not exist
#output = f.splitlines()
#print(output)
#with open("C:\learn-automation\learn-python-kirk\week2\show_version.txt") as f:
#    mylist = f.read()
#print(mylist)
#print('-'*80)
#print(mylist[0])
f= open("C:\learn-automation\learn-python-kirk\week2\extra_file.txt",mode='w')
f.write("something new\n")
f.write("something very new\n")
f.write("really new\n")
f.close()
f_read = open("C:\learn-automation\learn-python-kirk\week2\extra_file.txt")
#f = open("C:\learn-automation\learn-python-kirk\week2\extra_file.txt"
print(f_read.read())
print("-"*80)
f=open("C:\learn-automation\learn-python-kirk\week2\extra_file.txt",mode='a')
f.write("append new file\n")
f.close()
f = open("C:\learn-automation\learn-python-kirk\week2\extra_file.txt")
print(f.read())




#f.seek(0)
#f_output = f.read()
#print(f_output)
#print(f.read())
#print(f.seek(0))
# seek will move the cursor to the begining of the file
#print("-"*80)
#f.readline()
#print(f.readline())
#print(f.readlines())

#print(output)

#f.close()
