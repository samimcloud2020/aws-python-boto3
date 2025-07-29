from bs4 import BeautifulSoup
import requests
import pandas as pd
from urllib.parse import urljoin

def scrape_bsnl_website(url):
    try:
        # Send HTTP request with SSL verification disabled
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
        response = requests.get(url, headers=headers, verify=False)  # Disable SSL verification
        response.raise_for_status()  # Raise exception for bad status codes
        
        # Parse HTML content
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Extract page title
        page_title = soup.title.string.strip() if soup.title else 'No Title Found'
        
        # Extract all hyperlinks
        links = []
        for link in soup.find_all('a', href=True):
            href = link['href']
            # Convert relative URLs to absolute URLs
            full_url = urljoin(url, href)
            link_text = link.get_text(strip=True) or 'No Text'
            links.append({'Text': link_text, 'URL': full_url})
        
        # Create DataFrame
        df = pd.DataFrame(links)
        
        # Save to CSV
        output_file = 'bsnl_links.csv'
        df.to_csv(output_file, index=False, encoding='utf-8')
        
        # Print summary
        print(f"Page Title: {page_title}")
        print(f"Total Links Found: {len(links)}")
        print(f"Data saved to {output_file}")
        
        return df
    
    except requests.RequestException as e:
        print(f"Error fetching the webpage: {e}")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

if __name__ == "__main__":
    url = "https://bsnl.co.in/"
    # Suppress SSL warnings
    import urllib3
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    scraped_data = scrape_bsnl_website(url)
    if scraped_data is not None:
        print("\nFirst 5 links extracted:")
        print(scraped_data.head())
