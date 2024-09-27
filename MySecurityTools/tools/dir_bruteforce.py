import requests

def brute_force_directories(target_url, wordlist):
    with open(wordlist, 'r') as file:
        for line in file:
            dir = line.strip()
            url = f"{target_url}/{dir}"
            response = requests.get(url)
            if response.status_code == 200:
                print(f"Directory found: {url}")
