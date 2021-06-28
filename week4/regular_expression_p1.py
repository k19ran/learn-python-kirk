import re

ip_addr = "192.168.1.1"
ip_addr2 = "    192.168.1.1    "
print(re.search(r".",ip_addr))
#print(re.search(r"0",ip_addr))
print(re.search(r".",ip_addr).group(0))
print(re.search(r"..",ip_addr).group(0))
print(re.search(r"...",ip_addr).group(0))
print(re.search(r".+",ip_addr).group(0))
print(re.search(r".*",ip_addr).group(0))
print(re.search(r".*",""))
print(re.search(r".+",""))
print(re.search(r"^.+$",ip_addr).group(0))
print(re.search(r"^\d+",ip_addr).group(0))
print(re.search(r"\d$",ip_addr).group(0))
print(re.search(r"^\s+",ip_addr2).group(0))
print(re.search(r"^\s+",ip_addr2))
print(re.search(r"^\s+\S+",ip_addr2))
print(re.search(r"^\s+\S+",ip_addr2).group(0))
print(re.search(r"^\s+[\d]",ip_addr2).group(0))
print(re.search(r"^\s+[\d]+",ip_addr2).group(0))
print(re.search(r"^\s+[\d\.]+",ip_addr2).group(0))
print(re.search(r"^\s+(\S+)",ip_addr2).group(0))
print(re.search(r"^\s+(\S+)",ip_addr2).groups())
print(re.search(r"^\s+(\S+)",ip_addr2).group(1))
print(re.search(r"^\s+(\S+)",ip_addr2).group(0))



