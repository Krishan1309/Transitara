
from config import setup_perplexity
import requests

def generate_itinerary(destination, days, attractions):
    """Generate day-by-day plan"""
    config = setup_perplexity()
    headers = {
        "Authorization": f"Bearer {config['api_key']}",
        "Content-Type": "application/json"
    }
    
    prompt = f"""Create a {days}-day itinerary for {destination} covering these attractions:
    {[attr['name'] for attr in attractions]}
    Include time slots, transportation tips, and meal suggestions.
    Format:
    ### Day 1
    - [Time] [Activity] ([Location])
    - [Time] [Meal] ([Restaurant])
    """
    
    payload = {
        "model": config["model"],
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.7  
    }
    
    response = requests.post(
        f"{config['base_url']}/chat/completions",
        headers=headers,
        json=payload
    )
    return response.json()['choices'][0]['message']['content']

