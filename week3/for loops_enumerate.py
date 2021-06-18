ip_addr_list = ["11.11.11.11","12.12.12.12","13.13.13.13","14.14.14.14"]

for my_var in enumerate(ip_addr_list):
    print(my_var)
    #break
print(my_var)
print(type(my_var))
var1,var2 = my_var
print(var1)
print(var2)

for i,ip_addr in enumerate(ip_addr_list):
    print(i)
    print(ip_addr)
    print("-"*30)

