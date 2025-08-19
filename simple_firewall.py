# List of blocked IPs and Ports
blocked_ips = ["192.168.1.100", "10.0.0.5"]
blocked_ports = [22, 23]   # SSH and Telnet blocked

# Firewall function
def firewall(packet_ip, packet_port):
    if packet_ip in blocked_ips:
        return f"Blocked traffic from {packet_ip}"
    elif packet_port in blocked_ports:
        return f"Blocked traffic on port {packet_port}"
    else:
        return f"Allowed traffic from {packet_ip} on port {packet_port}"

# Take user input
packet_ip = input("Enter packet IP: ")
packet_port = int(input("Enter packet portNo: "))

# Run firewall check
result = firewall(packet_ip, packet_port)
print(result)
