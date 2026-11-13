import ipaddress

devices = [("Admission PC", "172.16.45.200/20"),("Lab printer", "10.0.15.255/21"),("X-ray server", "192.168.4.0/23"),("Clinic router", "203.0.113.10/29")]
for name, value in devices:
    iface = ipaddress.ip_interface(value); net = iface.network
    print(name)
    print("network:", net.network_address)
    print("broadcast:", net.broadcast_address)
    print("hosts:", net.network_address+1, "-", net.broadcast_address-1)
    print("valid host:", iface.ip not in (net.network_address, net.broadcast_address), "\n")
