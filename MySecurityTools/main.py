from tools.port_scanner import scan_ports
from tools.dir_bruteforce import brute_force_directories
from tools.whois_lookup import whois_lookup
from tools.ip_grabber import grab_ip_info
from tools.discord_token_grabber import grab_discord_tokens

def main():
    print("1. Scan de ports")
    print("2. Brute-force de répertoires")
    print("3. Whois lookup")
    print("4. IP Grabber")
    print("5. Discord Token Grabber")
    
    choice = input("Choisissez une option : ")
    
    if choice == '1':
        target = input("Entrez l'IP à scanner : ")
        scan_ports(target)
    elif choice == '2':
        target_url = input("Entrez l'URL cible : ")
        wordlist = input("Entrez le chemin vers le fichier wordlist : ")
        brute_force_directories(target_url, wordlist)
    elif choice == '3':
        domain = input("Entrez le nom de domaine : ")
        whois_lookup(domain)
    elif choice == '4':
        ip_address = input("Entrez une IP (laisser vide pour votre IP publique) : ")
        grab_ip_info(ip_address if ip_address else None)
    elif choice == '5':
        grab_discord_tokens()
    else:
        print("Choix invalide !")

if __name__ == "__main__":
    main()
