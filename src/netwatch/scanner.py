import socket
import psutil
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
    return "маска не найдена"
print(find_mask(get_local_ip()))

