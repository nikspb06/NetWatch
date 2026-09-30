import socket
import psutil
import ipaddress
from scapy.all import ARP, Ether, srp

def get_local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(("8.8.8.8", 80))
        local_ip = s.getsockname()[0]
    except Exception:
        local_ip = "127.0.0.1"
    finally:
        s.close()
    return local_ip



def find_mask(ip_to_find):
    interfaces = psutil.net_if_addrs()
    for interface_name, addresses in interfaces.items():
        for addr in addresses:
            if addr.address == ip_to_find:
                return addr.netmask
    return "mask is not find"

def find_interface(ip,mask):
    ip_interface = ipaddress.IPv4Interface(f"{ip}/{mask}")    
    return ip_interface

def find_network():
    int_addr = ipaddress.IPv4Interface(str(find_interface(get_local_ip(),find_mask(get_local_ip()))))
    network_addr = int_addr.network
    return network_addr

def find_active_local_devices():
    arp = ARP(pdst=str(find_network()))

    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether/arp

    result = srp(packet, timeout=3, verbose=0)[0]

    devices_list = []
    for sent, received in result:
        devices_list.append({'ip': received.psrc, 'mac': received.hwsrc})
        
    return devices_list


devices = find_active_local_devices()
print(devices,sep="\n")


