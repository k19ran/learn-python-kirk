'''
Create a list of five IP addresses.

Use the .append() method to add an IP address onto the end of the list. Use the .extend() method to add two more IP addresses to the
 end of the list.

Use list concatenation to add two more IP addresses to the end of the list.

Print out the entire list of ip addresses. Print out the first IP address in the list. Print out the last IP address in the list.

Using the .pop() method to remove the first IP address in the list and the last IP address in the list.

Update the new first IP address in the list to be '2.2.2.2'. Print out the new first IP address in the list.
'''

banner = "-" * 80

ip_list = ["11.11.11.11","12.12.12.12","13.13.13.13","14.14.14.14","15.15.15.15"]
print("First 5 ip addresses:{}".format(ip_list))
ip_list.append("16.16.16.16")
print("6 ip addresses:{}".format(ip_list))
ip_list.extend(["17.17.17.17","18.18.18.18"])
print("8 ip addresses:{}".format(ip_list))

new_ip_list = ip_list + ["19.19.19.19","20.20.20.20"]
print("New complete address list: {}".format(new_ip_list))
print("First address from the list: {}".format(new_ip_list[0]))
print("last address from the list: {}".format(new_ip_list[-1]))
new_ip_list.pop(0) # first address pop
new_ip_list.pop()# last adres pop
print("New list after pop:{}".format(new_ip_list))
new_ip_list[0] = "2.2.2.2"
print("New list after assiging 2.2.2.2:{}".format(new_ip_list))
print("First address in new list:{}".format(new_ip_list[0]))


