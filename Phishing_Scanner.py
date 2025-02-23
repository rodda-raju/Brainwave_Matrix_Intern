import requests
from bs4 import BeautifulSoup
import tldextract

# Define a list of known phishing URLs (In a real application, use a comprehensive database)
phishing_urls = ["example-phishing.com", "malicious-link.com"]

def extract_domain(url):
    domain_info = tldextract.extract(url)
    return f"{domain_info.domain}.{domain_info.suffix}"

def is_phishing_link(url):
    domain = extract_domain(url)
    if domain in phishing_urls:
        return True
    return False

def scan_url(url):
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')

        # Check links in the webpage
        links = soup.find_all('a', href=True)
        for link in links:
            if is_phishing_link(link['href']):
                return True, link['href']
        return False, None
    except requests.exceptions.RequestException as e:
        print(f"Error accessing {url}: {e}")
        return False, None

def main():
    url = input("Enter the URL to scan: ")
    is_phishing, malicious_link = scan_url(url)
    if is_phishing:
        print(f"Phishing link detected: {malicious_link}")
    else:
        print("No phishing links detected.")

if __name__ == "__main__":
    main()
