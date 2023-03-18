import os
import requests
from dotenv import load_dotenv
from random import sample

load_dotenv()

API_KEY = os.environ['PET_FINDER_API_KEY']
API_SECRET = os.environ['PET_FINDER_SECRET']

def get_api_token():
    resp = requests.post(
        'https://api.petfinder.com/v2/oauth2/token',
        data={"grant_type": 'client_credentials', "client_id": API_KEY, "client_secret": API_SECRET}
    )

    resp_data = resp.json()
    token = resp_data["access_token"]

    return token



def get_random_pet():
    resp = requests.get(
        "https://api.petfinder.com/v2/animals?limit=100",
        headers={'Authorization': f'Bearer {API_TOKEN}'})

    pet_data = resp.json()

    pet = sample(pet_data['animals'], 1)
    age = pet['age']
    name = pet['name']
    img_url = pet['photos'][0]['medium']

    return {"age": age, "name": name, "img_url": img_url}




