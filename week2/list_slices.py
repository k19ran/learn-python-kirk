#with open("C:\learn-automation\learn-python-kirk\week2\show_version.txt") as f:
#    mylist = f.read()
#print(mylist)

f = open("C:\learn-automation\learn-python-kirk\week2\show_version.txt")
output = f.readlines()
print(type(output))
print(output[0])
print(len(output))
print(output[0:5])
print(output[55:])
print('-'*80)
#print(output[:])
print(output[27:31])
#output would be from 27 till 30 by excluding 31
print(output[-4:-1])
print(output[-4:])
