net_device = {}
print(type(net_device))
net_device['ip_addr'] = "192.168.1.1"
var1 = 'vendor'
net_device[var1] = "cisco"
net_device["device_type"] = "cisco"
print(net_device)
net_device['vendor']="juniper"
print(net_device['vendor'])

net_device2 = net_device
print(net_device2 is net_device)