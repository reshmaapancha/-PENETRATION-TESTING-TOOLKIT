from modules import port_scanner, brute_forcer

def main():
    print("\n=== Penetration Testing Toolkit ===")
    print("1. Port Scanner")
    print("2. Brute Forcer (Web Login)")
    
    choice = input("Choose a module (1 or 2): ")

    if choice == '1':
        target_ip = input("Enter the target IP address: ")
        port_scanner.scan_ports(target_ip)
    elif choice == '2':
        brute_forcer.start_brute_force()
    else:
        print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    main()
