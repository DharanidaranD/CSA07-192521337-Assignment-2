import ipaddress
print('IPv6 shortest:',ipaddress.IPv6Address('2001:0db8:0000:0000:0000:ff00:0042:8329').compressed)
mac=[int(x,16) for x in '00:1A:2B:3C:4D:5E'.split(':')]; mac[0]^=2
eui=mac[:3]+[255,254]+mac[3:]
print('EUI-64:',':'.join(f'{x:02X}' for x in eui))
