ip_addr_list = ["11.11.11.11","12.12.12.12","13.13.13.13","14.14.14.14"]
ip_list2 = ["21.21.21.21","22.22.22.22","23.23.23.23","24.24.24.24"]

for ip in ip_addr_list:
    print(ip)
print("-"*80)
for ip in ip_addr_list:
    print(ip)
    if ip == "11.11.11.11":
        break
print("-"*80)    
for ip in ip_addr_list:
    print(ip)
    if ip == "15.15.15.15":
        break
    else:
         print("else block executed")
print("-"*80)    
for ip in ip_addr_list:
    print(ip)
    if ip == "15.15.15.15":
        break
else:
    print("else block executed")

print("-"*80)    

while True:
    print("Hello")
    print("World")
    if ip_list2 [0] == "21.21.21.21":
        break