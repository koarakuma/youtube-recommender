import json 
import requests

with open('creds.json', 'r') as f:
    creds = json.load(f)


API_KEY = (creds['key'])

url = "https://www.googleapis.com/youtube/v3/search" #this is the base url for the youtube api we add parameters to the url to get the search we want
params = {
    "part": "snippet",
    "q": "minecraft gameplay",  # your search term or what specifically you want to watch
    "type": "video", #this is the type of content we want to search for
    "maxResults": 5, #this is the maximum number of results we want to get
    "key": API_KEY #this is the api key we got from the youtube api
}

response = requests.get(url, params=params) #this is the request to the youtube api and the specific response we get back
data = response.json() #we take our response and store it in a json format

for item in data["items"]: #we iterate through the items in the data
    print(item["snippet"]["title"], "https://youtube.com/watch?v=" + item["id"]["videoId"]) #we print the title and the url of the video
