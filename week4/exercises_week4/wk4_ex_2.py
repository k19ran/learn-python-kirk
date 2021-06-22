'''
Prompt a user to enter in an IP address from standard input. Read the IP address in and break it up into its octets. Print out the octets in decimal, binary, and hex.

Your program output should look like the following:
​ $ python exercise2.py 
Please enter an IP address: 80.98.100.240

Octet1         Octet2         Octet3         Octet4     
------------------------------------------------------------
      80             98             100            240      
   0b1010000      0b1100010      0b1100100     0b11110000   
     0x50           0x62           0x64           0xf0      
------------------------------------------------------------

Four columns, fifteen characters wide, a header column, data centered in the column.
'''
ip_addr=input("Please enter an IP address:")
my_var = ip_addr.split('.')
print("{:^20}{:^20}{:^20}{:^20}".format("Octet1", "Octet2", "Octet3", "Octet4"))
print('-'*80)
#print("{:^20}{:^20}{:^20}{:^20}".format(my_var[0],my_var[1],my_var[2],my_var[3]))
print("{:^20}{:^20}{:^20}{:^20}".format(*my_var))
print("{:^20}{:^20}{:^20}{:^20}".format(hex(int(my_var[0])),hex(int(my_var[1])),hex(int(my_var[2])),hex(int(my_var[3]))))
print("{:^20}{:^20}{:^20}{:^20}".format(bin(int(my_var[0])),bin(int(my_var[1])),bin(int(my_var[2])),bin(int(my_var[3]))))
print('-'*80)
print()