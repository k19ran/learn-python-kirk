ip_addr_list = ["11.11.11.11","12.12.12.12","13.13.13.13","14.14.14.14"]
ip_list2 = ["21.21.21.21","22.22.22.22","23.23.23.23","24.24.24.24"]

for ip in ip_addr_list:
    print(ip)
    if ip == "13.13.13.13":
        break

for ip in ip_addr_list:
    print("hello")
    if ip == "13.13.13.13":
        continue
    print(ip)

for ip3 in ip_addr_list:
    print("\n")
    print("hello")
    print(ip3)
    print("-"*20)
    
    for ip4 in ip_list2:
        print(ip4)

for ip in ip_addr_list:
    pass

print(list(range(10)))
print(list(range(10,20)))

print(range(20))

for my_var in range(10):
    print(my_var)

print("21.21.21.21" in ip_list2)

