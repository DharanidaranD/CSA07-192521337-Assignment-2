import math, ipaddress

def to_int(ip):
    a,b,c,d=map(int,ip.split('.')); return (a<<24)|(b<<16)|(c<<8)|d

def to_ip(n): return '.'.join(str((n>>s)&255) for s in (24,16,8,0))

def vlsm(base, needs):
    addr=to_int(base)
    for name,hosts in sorted(needs,key=lambda x:-x[1]):
        block=1
        while block<hosts+2: block*=2
        prefix=32-int(math.log2(block))
        print(f'{name:<12} {to_ip(addr)}/{prefix} hosts {to_ip(addr+1)} - {to_ip(addr+block-2)} bcast {to_ip(addr+block-1)}')
        addr+=block
    return to_ip(addr)

needs=[('Labs',100),('Staff',50),('Library',25),('WAN link',2)]
print('next free address:',vlsm('192.168.10.0',needs))
print('\nVerification:')
for s in ['192.168.10.0/25','192.168.10.128/26','192.168.10.192/27','192.168.10.224/30']:
    n=ipaddress.ip_network(s); print(n,n.network_address+1,n.broadcast_address-1,n.broadcast_address)
