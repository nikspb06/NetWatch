import socket

def port_scaner(ip,port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)

    result = sock.connect_ex((ip, port))

    sock.close()

    if result == 0:
        return True

    return False

def scan_local_devices_ports(ip,ports):
    open_device_ports = list()

    for port in ports:
        if port_scaner(ip,port) == True:
            open_device_ports.append(port)
        
    return open_device_ports


func = scan_local_devices_ports("192.168.0.1",[-1])
print(func)
