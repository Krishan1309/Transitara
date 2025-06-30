import requests
from config import setup_perplexity

def get_top_attractions(destination):
    """Fetch top attractions using Perplexity API"""
    config = setup_perplexity()
    headers = {
        "Authorization": f"Bearer {config['api_key']}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": config["model"],
        "messages": [{
            "role": "user",
            "content": f"List top 10 attractions in {destination} with 5-word descriptions. Format: Name|Description"
        }],
        "max_tokens": 300  
    }

    try:
        response = requests.post(
            f"{config['base_url']}/chat/completions",
            headers=headers,
            json=payload
        )
        response.raise_for_status()
        return parse_attractions(response.json()['choices'][0]['message']['content'])
    except Exception as e:
        print(f"API Error: {str(e)}")
        return []

def parse_attractions(raw_text):
    """Convert API response to structured data"""
    attractions = []
    for line in raw_text.split('\n'):
         if '|' in line:
             name, desc = line.split('|', 1)
             attractions.append({"name": name.strip(), "description": desc.strip()})
    return attractions
