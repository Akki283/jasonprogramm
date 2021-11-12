import requests
import json

r = requests.get("https://ip-ranges.amazonaws.com/ip-ranges.json")
j=r.json()
print(j)