import socket

def scan_ports(ports):
    """
    Scan specified ports on localhost.
    """
    print("Scanning ports on localhost...")
    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  # Set timeout for connection attempt
        result = sock.connect_ex(("localhost", port))
        if result == 0:
            print(f"Port {port} is open")
        sock.close()

if __name__ == "__main__":
    # Define the list of ports to scan on localhost
    ports = [80, 443, 8080]  # Add more ports as needed

    # Scan ports on localhost
    scan_ports(ports)
