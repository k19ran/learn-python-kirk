'''
Read the "show_vlan.txt" file into your program. Loop through the lines in this file and extract all of the VLAN_ID, VLAN_NAME combinations. From these VLAN_ID and VLAN_NAME construct a new list where each element in the list is a tuple consisting of (VLAN_ID, VLAN_NAME). Print this data structure to the screen.
Your output should look as follows:
[('1', 'default'),
 ('400', 'blue400'),
 ('401', 'blue401'),
 ('402', 'blue402'),
 ('403', 'blue403')]
'''
from pprint import pprint

banner = "-"*40

with open("C:\learn-automation\learn-python-kirk\week3\show_vlan.txt",mode="r") as f:
    mylist = f.readlines()
banner = "-"*40    

fields=[]
vlan_list= []

for list in mylist:
    if "VLAN" in list or "---" in list or list.startswith("   "):
        continue
    fields = list.split()
    pprint(fields)
    vlan_id = fields[0]
    vlan_name = fields[1]
    vlan_list.append((vlan_id,vlan_name))
    #pprint(vlan_list)

pprint(vlan_list)
