import urllib.request
import json

url = urllib.request.urlopen("https://catfact.ninja/fact")
json = json.load(url)
print(json)
