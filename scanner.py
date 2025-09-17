import ipaddress
import scapy.all as scapy
import socket
import threading
from queue import Queue

def discover_hosts(cidr):
    """Discover live hosts via ARP requests and return list of dicts with IP, MAC, hostname."""
    results_queue = Queue()
    threads = []

    def scan(ip):
        try:
            arp = scapy.ARP(pdst=ip)
            ether = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
            pkt = ether / arp
            answered = scapy.srp(pkt, timeout=3, verbose=False)[0]

            for _, recv in answered:
                info = {
                    'ip': recv.psrc,
                    'mac': recv.hwsrc
                }
                try:
                    info['hostname'] = socket.gethostbyaddr(info['ip'])[0]
                except socket.herror:
                    info['hostname'] = "Unknown"
                results_queue.put(info)
        except Exception as e:
            print(f"Error scanning {ip}: {e}")

    network = ipaddress.ip_network(cidr, strict=False)
    for ip in network.hosts():
        t = threading.Thread(target=scan, args=(str(ip),))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

    hosts = []
    while not results_queue.empty():
        hosts.append(results_queue.get())
    return hosts

def scan_ports(ip, start_port, end_port):
    """Scan TCP ports for a single IP."""
    open_ports = []

    def worker(port):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)
        try:
            if s.connect_ex((ip, port)) == 0:
                open_ports.append(port)
        finally:
            s.close()

    threads = []
    for p in range(start_port, end_port + 1):
        t = threading.Thread(target=worker, args=(p,))
        t.start()
        threads.append(t)
    for t in threads:
        t.join()
    return open_ports
