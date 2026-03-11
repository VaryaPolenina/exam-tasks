from ipaddress import*
ip_net = ip_network('212.170.112.0/255.255.240.0', 0)
count = 0
for i in ip_net:
    if f'{i:b}'.count('1') != f'{i:b}'.count('0'):
        count += 1
print(count)
