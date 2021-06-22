net_device = {'ip_addr': '192.168.1.1', 'vendor': 'cisco', 'device_type': 'cisco'}
print(net_device)
print(net_device.get('vendor'))
print(net_device.get('ios'))
print(net_device.get('ios','987'))
net_device2 = net_device.copy()
print(net_device2)
print(net_device2 is net_device)
net_device['model'] = '1941'
print(net_device)
print(net_device.pop('model'))
print(net_device2)
net_device2 = {"model":"3750"}
#print(net_device2)
net_device.update(net_device2)
print(net_device2)
print(net_device)
net_device2 = {"vendor":"juniper","model":"srx"}
net_device.update(net_device2)
print(net_device)

for key in net_device:
    print(key)

for v in net_device.values():
    print(v)

for k,v in net_device.items():
    print(k)
    print(v)
    print('-'*30)
