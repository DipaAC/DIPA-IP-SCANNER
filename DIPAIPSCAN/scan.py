import socket
import requests

def print_ascii_art():
    ascii_art = r"""


________  ._____________  _____    ._____________    __________________     _____    _______    _______  _____________________ 
\______ \ |   \______   \/  _  \   |   \______   \  /   _____/\_   ___ \   /  _  \   \      \   \      \ \_   _____/\______   \
 |    |  \|   ||     ___/  /_\  \  |   ||     ___/  \_____  \ /    \  \/  /  /_\  \  /   |   \  /   |   \ |    __)_  |       _/
 |    `   \   ||    |  /    |    \ |   ||    |      /        \\     \____/    |    \/    |    \/    |    \|        \ |    |   \
/_______  /___||____|  \____|__  / |___||____|     /_______  / \______  /\____|__  /\____|__  /\____|__  /_______  / |____|_  /
        \/                     \/                          \/         \/         \/         \/         \/        \/         \/ 


     DipaIpScanner
                                               
    """
    print(ascii_art)

def check_domain(domain):
    try:
        # Resolving domain to an IP address
        ip = socket.gethostbyname(domain)
        print(f"[INFO] {domain} resolved to {ip}")
    except socket.gaierror:
        print(f"[ERROR] Unable to resolve domain: {domain}")
        return False

    try:
        # Checking if the domain responds to an HTTP request
        response = requests.get(f"http://{domain}", timeout=5)
        print(f"[INFO] {domain} is active with status code {response.status_code}")
        return True
    except requests.RequestException as e:
        print(f"[ERROR] Unable to connect to {domain}: {e}")
        return False

if __name__ == "__main__":
    print_ascii_art()
    print("Domain Scanner Tool")
    print("-------------------")

    # Input: list of domains to scan
    domains = input("Enter domains to scan (comma-separated): ").split(",")
    domains = [domain.strip() for domain in domains]

    print("\nScanning domains...\n")
    for domain in domains:
        check_domain(domain)

    print("\nScan complete.")