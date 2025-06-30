import os
from dotenv import load_dotenv

def setup_perplexity():
    """Configure Perplexity API settings"""
    load_dotenv()
    api_key = os.getenv("PPLX_API_KEY")
    if not api_key:
        raise ValueError("Missing PPLX_API_KEY in .env file")
    return {
        "api_key": api_key,
        "base_url": "https://api.perplexity.ai",
        "model": "sonar-pro"
    }