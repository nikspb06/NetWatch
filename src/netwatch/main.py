import argparse
from scanner import find_active_local_devices
from port_scanner import scan_local_devices_ports
def main():
    parser = argparse.ArgumentParser(description="NetWatch")
    parser.add_argument("command", choices=["scan", "ports"])
    parser.add_argument("ip", nargs="?")

    args = parser.parse_args()

    if args.command == "scan":
        devices = find_active_local_devices()
        for i in devices:
            print(i)


    elif args.command == "ports":
        ports = [22, 80, 443]
        open_ports = scan_local_devices_ports(args.ip, ports)
        print(open_ports)

if __name__ == "__main__":
    main()