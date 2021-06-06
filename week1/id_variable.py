ip_addr = '192.168.1.1'
print(id(ip_addr))
ip_addr2 = '10.1.1.1'
print(id(ip_addr2))
ip_addr2 = ip_addr
print(id(ip_addr2))