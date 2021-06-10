ip_addr1 = '1.1.1.1'
ip_addr2 = '1.1.1.2'
ip_addr3 = '1.1.1.3'
print("\n")
print('-'*80)
print(ip_addr1,ip_addr2,ip_addr3)
print("{}{}{}".format(ip_addr1,ip_addr2,ip_addr3))
print("{:20}{:20}{:20}".format(ip_addr1,ip_addr2,ip_addr3))
print("{:>20}{:>20}{:>20}".format(ip_addr1,ip_addr2,ip_addr3))
print("{:<20}{:<20}{:<20}".format(ip_addr1,ip_addr2,ip_addr3))
#positional arguments
print("{:^20}{:^20}{:^20}".format(ip_addr1,ip_addr2,ip_addr3))
#named arguments
print("{my_ip:^20}{ip:^20}{ip_alt:^20}".format(ip=ip_addr1,ip_alt=ip_addr2,my_ip=ip_addr3))
print('-'*80)
ip_addr4 = '1.1.1.4'
octets = ip_addr4.split('.')
print("\n")
print('-'*80)
print(octets)
print("{:^20}{:^20}{:^20}{:^20}".format(octets[0],octets[1],octets[2],octets[3]))
print('-'*80)
#print("{:^20}{:^20}{:^20}{:^20}".format(octets))
#print("{:^20}{:^20}{:^20}{:^20}".format(str(octets)))
print("{:^20}{:^20}{:^20}{:^20}".format(*octets))