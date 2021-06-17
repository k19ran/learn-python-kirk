'''
Read in the "show_arp.txt" file using the readlines() method. Use a list slice to remove the header line.

Use pretty print to print out the resulting list to the screen, syntax is:
from pprint import pprint
pprint(some_var)
Use the list .sort() method to sort the list based on IP addresses.

Create a new list slice that is only the first three ARP entries.

Use the .join() method to join these first three ARP entries back together as a single string using the newline character ('\n') 
as the separator.

Write this string containing the three ARP entries out to a file named "arp_entries.txt"
'''
from pprint import pprint
banner = "-"*80

with open("C:\learn-automation\learn-python-kirk\week2\show_arp.txt") as file:
    output = file.readlines()

pprint(output)
print(banner)
sliced_output = output[1:]
pprint(sliced_output)
print(banner)
sliced_output.sort()

new_arp_list = sliced_output[0:3]
pprint(new_arp_list)    
print(banner)

join_list = "\n".join(new_arp_list)
pprint(join_list)
print(banner)

with open("C:\learn-automation\learn-python-kirk\week2\extra_arp_str.txt", mode ='w') as new_file:
    new_file.write(join_list)
#new_file.close()
with open("C:\learn-automation\learn-python-kirk\week2\extra_arp_str.txt", mode ='r') as newest_file:
    newest_file = newest_file.read()

pprint(newest_file)
#new_file.close()



