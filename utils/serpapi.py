# utils/serpapi.py
import requests

def get_home_depot_product(product_name, api_key):
    url = "https://serpapi.com/search"
    params = {
        "engine": "home_depot",
        "q": product_name,
        "api_key": api_key,
        "limit":10
    }
    
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        response.raise_for_status()
