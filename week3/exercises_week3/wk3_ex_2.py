'''
Read the contents of the "show_arp.txt" file. Using a for loop, iterate over the lines of this file. Process the lines of the file and separate out the ip_addr and mac_addr for each entry into a separate variable.

Add a conditional statement that searches for '10.220.88.1'. If 10.220.88.1 is found, print out the string "Default gateway IP/Mac" and the corresponding IP address and MAC Address.

Using a conditional statement, also search for '10.220.88.30'. If this IP address is found, then print out "Arista3 IP/Mac is" and the corresponding ip_addr and mac_addr.

Keep track of whether you have found both the Default Gateway and the Arista3 switch. Once you have found both of these devices, 'break' out of the for loop.
'''
from pprint import pprint

banner = "-"*40

with open("C:\learn-automation\learn-python-kirk\week3\show_arp.txt",mode="r") as f:
    mylist = f.readlines()

new_list = []
fields =[]

found1,found2 = (False,False)

for list in mylist:
    if "Protocol" in list:
        continue
    new_list = list.split()
    fields = new_list[1],new_list[3]
    ip_addr = new_list[1]
    mac_addr = new_list[3]
    if fields[0] == "10.220.88.1":
        print("Default gateway IP/Mac:{} {}".format(ip_addr,mac_addr))
        found1 = True
    elif fields[0] == "10.220.88.30":
        print("Arista3 IP/Mac is:{} {}".format(ip_addr,mac_addr))
        found2 = True
    if found1 and found2:
        print("Exsiting")
        break

    



