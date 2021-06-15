ipv6_addr = "2a01:0db8:85a3:0020:0500:8a2e:0370:7334"
words = ipv6_addr.split(":")
print(words)
output = "::".join(words)
print(output)
ip_addr = "192.168.10.10"
split = ip_addr.split(".")
print(split)
output_1 = "...".join(split)
print(output_1)