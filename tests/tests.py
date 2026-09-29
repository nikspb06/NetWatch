import ipaddress
interface = ipaddress.ip_interface("192.168.1.25/24")
print(dir(interface))