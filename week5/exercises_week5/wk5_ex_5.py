'''
Read the 'show_ip_bgp_summ.txt' file into your program. From this BGP output obtain the first and last lines of the output.

From the first line use the string .split() method to obtain the local AS number.

From the last line use the string .split() method to obtain the BGP peer IP address.

Print both local AS number and the BGP peer IP address to the screen.
'''
from pprint import pprint

with open("C:\learn-automation\learn-python-kirk\week2\show_bgp_summary.txt", mode ='r') as f:
    my_list = f.readlines()

pprint(my_list)
new_list = my_list[0]
last_list = my_list[-1]
pprint(new_list)
pprint(last_list)
as_list = new_list.split()
print("AS number:{}".format(as_list[-1]))
peer_list = last_list.split()
print("Peer ip addres:{}".format(peer_list[0]))
