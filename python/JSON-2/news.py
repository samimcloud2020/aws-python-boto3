import requests
import json
from typing import Optional, List, Dict
from requests.exceptions import RequestException

class NewsAPIError(Exception):
    pass

def fetch_news_data(api_key: str, country: str="us", category: str="business"):
    base_url = "https://newsapi.org/v2/top-headlines"
    params = {"country": country, "category": category, "apiKey": api_key}

    try:
        response = requests.get(base_url, params=params, timeout=5)
        response.raise_for_status()
        
        try:
            news_data = response.json()
        except json.JSONDecodeError as e:
            raise NewsAPIError(f"Error decoding json response {e}")
        
        #validate the expected data structure
        if not isinstance(news_data, dict) or news_data.get("status") != "ok":
            raise NewsAPIError("Invalid news data format or status is not ok")
        
        processed_articles=[]
        for article in news_data.get("articles", []):
            processed_articles.append({
                "source_name": article.get("source", {}).get("name"),
                "author": article.get("author"),
                "title": article.get("title"),
                "description": article.get("description"),
                "url": article.get("url"),
                "published_at": article.get("publishedAt")
            })

        return {
                "status": news_data.get("status"),
                "total_results": news_data.get("totalResults"),
                "articles": processed_articles
            }    
    except RequestException as e:
        print(f"Network error occured: {e}")
        return None
    except NewsAPIError as e:
        print(f"News Api Error: {e}")
        return None
    except Exception as e:
        print(f"Unexpected error : {e}")
        return None


def save_news_data(data: Dict, filename: str) -> bool:
    try:
        with open(filename, 'w') as f:  # Fixed: Use filename parameter instead of 'filename'
            json.dump(data, f, indent=4)   #json.dump() (dump to file)   and json.dumps() (dump to string)
        return True
    except (IOError, TypeError) as e:
        print(f"Error saving news data: {e}")
        return False  # Fixed: Use False instead of false

def load_news_data(filename: str) -> Optional[Dict]:
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error loading news data: {e}")
        return None
    
def display_news_summary(data: Dict) -> None:
    if not data or not data.get("articles"):
        print("No news data to display")
        return
        
    print(f"Total Articles: {data.get('total_results')}")
    print("\nTop Headlines:")
    for i, article in enumerate(data.get("articles", []), 1):
        print(f"\n{i}. {article.get('title')}")
        print(f"Source: {article.get('source_name')}")
        print(f"Author: {article.get('author') or 'Unknown'}")
        print(f"Published: {article.get('published_at')}")
        print(f"Description: {article.get('description') or 'No description'}")
        print(f"URL: {article.get('url')}")



if __name__ == "__main__":
    api_key = "1d38501366bf45ad83a296269ac8ce5e"
    country = "us"
    category = "business"

    try:
        news_data = fetch_news_data(api_key=api_key, country=country, category=category)
        #print(f"news data is : {news_data}")    

        if news_data:
            # Display summary
            display_news_summary(news_data)
        
        # Save to JSON file
        if save_news_data(news_data, 'news_data.json'):
            print("\nNews data saved successfully to 'news_data.json'")
            
        # Load and verify saved data
        loaded_data = load_news_data('news_data.json')
        if loaded_data:
            print("\nSuccessfully loaded saved news data")
        else:
            print("Failed to fetch news data")


    except NewsAPIError as e:
        print(f"News API Error: {e}")
    except ValueError:
        print("ValueError: An invalid value was encountered.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        print("Job complete.")
