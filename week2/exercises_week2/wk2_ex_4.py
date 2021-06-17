'''
Read in the "show_ip_int_brief.txt" file into your program using the .readlines() method.

Obtain the list entry associated with the FastEthernet4 interface. You can just hard-code the index at this point since we haven't 
covered for-loops or regular expressions. Use the string .split() method to obtain both the IP address and the corresponding interface
associated with the IP.

Create a two element tuple from the result (intf_name, ip_address).

Print that tuple to the screen.

Use pycodestyle on this script. Get the warnings/errors to zero. You might need to 'pip install pycodestyle' on your computer
 (you should be able to type this from the shell prompt). Alternatively, you can type 'python -m pip install pycodestyle'.
'''
from pprint import pprint
banner = "-"*80
#my_tuple = []
with open("C:\learn-automation\learn-python-kirk\week2\show_ip_int_brief.txt", mode ='r') as f:
    my_list = f.readlines()
pprint(my_list)
print(banner)

intf_4 = my_list[5]
print(intf_4)
split_4 = intf_4.split()
print(split_4)
intf=split_4[0]
ip_addr=split_4[1]
my_tuple = (intf,ip_addr)
print(my_tuple)


