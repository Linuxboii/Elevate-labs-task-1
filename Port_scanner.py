import nmap
import subprocess
from prettytable import PrettyTable

def scan_network(subnet="192.168.1.0/24"):
    print(f"[*] Scanning network: {subnet}")
    scanner = nmap.PortScanner()
    scanner.scan(hosts=subnet, arguments='-p 1-1024 --open')

    table = PrettyTable()
    table.field_names = ["Host", "Protocol", "Port", "State", "Service"]

    for host in scanner.all_hosts():
        for proto in scanner[host].all_protocols():
            ports = scanner[host][proto].keys()
            for port in sorted(ports):
                state = scanner[host][proto][port]['state']
                service = scanner[host][proto][port]['name']
                table.add_row([host, proto, port, state, service])
    
    print(table)

def check_tshark():
    try:
        output = subprocess.check_output(["tshark", "-D"]).decode()
        print("[+] Tshark is installed and ready.")
    except FileNotFoundError:
        print("[!] Tshark is not installed. Please install it to use packet capture.")

if __name__ == "__main__":
    check_tshark()
    scan_network("192.168.1.0/24")  # Change the subnet as per your local network
