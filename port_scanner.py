import socket

def scan_ports(ip):
    print(f"\n[~] Scanning ports on {ip}...\n")
    for port in range(1, 1025):
        try:
            s = socket.socket()
            s.settimeout(0.5)
            result = s.connect_ex((ip, port))
            if result == 0:
                print(f"[+] Port {port} is OPEN")
            s.close()
        except socket.error:
            print(f"[!] Could not connect to {ip}")
            break
