import nmap

def scan_ports(target):
    scanner = nmap.PortScanner()
    scanner.scan(target, '1-1024')
    for host in scanner.all_hosts():
        print(f'Host : {host} ({scanner[host].hostname()})')
        print(f'State : {scanner[host].state()}')
        for proto in scanner[host].all_protocols():
            print(f'Protocol : {proto}')
            ports = scanner[host][proto].keys()
            for port in ports:
                print(f'Port : {port}\tState : {scanner[host][proto][port]["state"]}')
