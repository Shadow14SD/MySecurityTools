import requests

def grab_ip_info(ip_address=None):
    if ip_address is None:
        response = requests.get('https://ipinfo.io')
    else:
        response = requests.get(f'https://ipinfo.io/{ip_address}')
    
    if response.status_code == 200:
        data = response.json()
        print(f"IP: {data['ip']}")
        print(f"Ville: {data.get('city', 'Inconnue')}")
        print(f"Région: {data.get('region', 'Inconnue')}")
        print(f"Pays: {data.get('country', 'Inconnu')}")
        print(f"Fournisseur Internet: {data.get('org', 'Inconnu')}")
        print(f"Localisation: {data.get('loc', 'Inconnue')}")
    else:
        print("Impossible de récupérer les informations IP.")
