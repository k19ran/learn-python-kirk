'''
Read the 'show_lldp_neighbors_detail.txt' file. 
Loop over the lines of this file. 
Keep reading the lines until you have encountered the remote "System Name" and remote "Port id". 
Save these two items into variables and print them to the screen. 
You should extract only the system name and port id from the lines (i.e. your variables should only have 'twb-sf-hpsw1' and '15'). Break out of your loop once you have retrieved these two items.
'''

from pprint import pprint

banner = "-"*40
system_name,port_id = (None,None)

with open("C:\learn-automation\learn-python-kirk\week3\show_lldp_neighbors_detail.txt",mode="r") as f:
    lldp = f.readlines()

fields = []

for list in lldp:
    if "system name" in list.lower():
        system_name = list.split("System Name: ")
    elif "port id" in list.lower():
        port_id = list.split("Port id: ")
    if system_name and port_id:
        break
#print(system_name[1],port_id[1])

print("System Name:{}".format(system_name[1]))
print("Port id:{}".format(port_id[1]))



print(banner)