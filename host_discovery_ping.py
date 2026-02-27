from scapy.all import*

ip = IP()
icmp = ICMP()
pingPckt = ip/icmp
addr = "10.10.10."

ipList = []

print(f"Tarama Başlatıldı: {addr}0/24")

for i in range(255):
    pingPckt[IP].dst=addr+str(i)
    print(pingPckt[IP].dst)
    response = sr1(pingPckt, timeout=0.5, verbose=0)
    
    if (response):
        # print(f"[+] Host Aktif:{pingPckt[IP].dst}")
        ipList.append(pingPckt[IP].dst)
    else:
        pass
        
print(ipList)