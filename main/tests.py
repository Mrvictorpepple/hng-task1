from django.test import TestCase
import requests
# Create your tests here.

URL = 'http://127.0.0.1:8000/'

get_response = requests.get(URL)
print(get_response.json())








