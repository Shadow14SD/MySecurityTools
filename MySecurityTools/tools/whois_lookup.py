import whois

def whois_lookup(domain):
    domain_info = whois.whois(domain)
    print(domain_info)
