#my_path = "c:\windows\newdorr\test\whatever"
#print(my_path)
my_path = r"c:\windows\newdorr\test\whatever"
print(my_path)
my_str1 = 'what ever'
my_str2 = "hello"
my_str3 = ''' this is multipl
line '''
my_str4 = """this is also 
multiple 
lne"""
print(my_str1)
print(my_str2)
print(my_str3)
print(my_str4)
print(repr(my_str3))
my_str = '   whatever, somethings else\n\n\n'
print(my_str)
print(my_str.strip())
print(my_str.lstrip())
print(my_str.rstrip())
ip_addr = '192.168.1.1'
print(ip_addr.split("."))
print(ip_addr.split('168.'))
print(ip_addr.split('192.'))
sentence = "this is a sample sentence"
print(sentence.split())
paragraph = """ this is
what is
called 
a split
paragraph"""
print(paragraph.split())
print(paragraph.split("\n"))
print(paragraph.splitlines()) 