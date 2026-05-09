import requests

API_KEY = "RKsW2jtYaYDszFRA8SIukjJhp1ujBVANslLfZe1g"

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