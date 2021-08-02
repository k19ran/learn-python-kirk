with open("C:\learn-automation\learn-python-kirk\week4\show_version.txt") as f:
    output = f.read()

#print(output)

show_ver = output.splitlines()
line = show_ver[0]
print(line)

import re

print(re.search(r"^C.*$",line))
print(re.search(r"^C.*$",line).group(0))
#print(re.search(r"^C.*$",line).group(1))
print(re.search(r"^Cisco (.*), Version (\S+),.*$",line).group(1))
print(re.search(r"^Cisco (.*), Version (\S+),.*$",line).group(2))
print(re.search(r"^Cisco (.*), Version (\S+), (.*)$",line).group(3))
os_version = re.search(r"^Cisco (.*), Version (\S+),.*$",line).group(2)
print(os_version)
print(re.search(r"^Cisco (.*), Version (?P<serial_num>\S+),.*$",line))
match = re.search(r"^Cisco (.*), Version (?P<serial_num>\S+),.*$",line)
print(match.groupdict())

