import json 
import requests
import random

with open('topics.json', 'r') as f:
    topics = json.load(f)
with open('creds.json', 'r') as f:
    creds = json.load(f)
with open('querys.json', 'r') as f:
    querys = json.load(f)

def findQuery():
    qMax = 0
    maxQuery = ""
    if len(querys) == 0:
        return(random.choice(topics['topics']))
    for query in querys:
        if querys[query] > qMax:
            qMax = querys[query]
            maxQuery = query
    if len(maxQuery) > 0:
        return(maxQuery)
    else:
        return(random.choice(topics['topics']))
def findEngagement(recommendations):
    like = input("Did you like the video? (y/n) ")
    for recommendation in recommendations["items"]:  
        title = recommendation["snippet"]["title"]
        words = title.split()
        for word in words:
            reshapeword = word.strip().capitalize()
            if like.lower() == "y":
                querys[reshapeword] = querys.get(reshapeword, 0) + 1
            else:
                querys[reshapeword] = querys.get(reshapeword, 0) - 1
    with open("querys.json", "w") as f:
        json.dump(querys, f, indent=4)



        

API_KEY = (creds['key'])

url = "https://www.googleapis.com/youtube/v3/search" #this is the base url for the youtube api we add parameters to the url to get the search we want



params = {
    "part": "snippet",
    "q": findQuery(),  # your search term or what specifically you want to watch
    "type": "video", #this is the type of content we want to search for
    "maxResults": 1, #this is the maximum number of results we want to get
    "key": API_KEY #this is the api key we got from the youtube api
}


response = requests.get(url, params=params) #this is the request to the youtube api and the specific response we get back
recommendations= response.json() #we take our response and store it in a json format


for item in recommendations["items"]: #we iterate through the items in the data
    print(item["snippet"]["title"], "https://youtube.com/watch?v=" + item["id"]["videoId"]) #we print the title and the url of the video

findEngagement(recommendations)

