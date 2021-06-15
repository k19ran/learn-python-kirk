my_list = []
print(type(my_list))
my_list = ['whatever','22',21,23.2]
print(my_list[0])
print(my_list[2])
my_list[1] = 'something'
print(my_list)
my_list.append('hello')
print(my_list)
print(len(my_list))
my_new_list = my_list + [89,'hey']
print(my_new_list)
my_list = my_new_list
print(my_list)
print(my_new_list)
print(my_list.pop())
print(my_list)
my_list.extend(['hey','how'])
print(my_list)
my_list.append(65)
print(my_list)
my_list.pop(1)
print(my_list)
del my_list[0]
print(my_list)
print(dir(my_list))
#my_list.sort()
#print(my_list)
my_list.extend([65,89])
print(my_list.count(65))
print(my_list.index(65))
my_list.remove(65)
print(my_list)