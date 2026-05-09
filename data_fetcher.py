import requests
import os
from dotenv import load_dotenv


def fetch_data(animal_name):
    """
    Fetches the animals data for the animal 'animal_name'.
    Returns: a list of animals, each animal is a dictionary:
    {
      'name': ...,
      'taxonomy': {
      ...
        },
    'locations': [
      ...
      ],
    'characteristics': {
      ...
      }
    },
    """
    load_dotenv()
    API_KEY = os.getenv('API_KEY')
    
    if not API_KEY:
        raise ValueError(
        "API_KEY not found. Please add your API key to the .env file."
        )
    
    url = f"https://api.api-ninjas.com/v1/animals?name={animal_name}"
    headers = {"X-Api-Key": API_KEY}
    data = requests.get(url, headers=headers).json()
    
    if not data:
        data = [{
            "name" : animal_name,
            "taxonomy" : "Not Found"    
                }]
    
    print("Data fetched.")
    return data