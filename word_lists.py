import requests
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv('API_KEY')
url = "https://random-words5.p.rapidapi.com/getMultipleRandom"
querystring = {"count":"10"}
headers = {
	"x-rapidapi-key": f"{API_KEY}",
	"x-rapidapi-host": "random-words5.p.rapidapi.com"
}
response = requests.get(url, headers=headers, params=querystring)
word_list = response.json()