import json
import requests

def api_get_request(url):
    # In this exercise, you want to call the last.fm API to get a list of the
    # top artists in Spain. The grader will supply the URL as an argument to
    # the function; you do not need to construct the address or call this
    # function in your grader submission.
    # 
    # Once you've done this, return the name of the number 1 top artist in
    # Spain. 
    
    #rjson = requests.get(url).json()
    rtext = requests.get(url).text
    rjson = json.loads(rtext)    
    topartists = rjson['topartists']
    first_artist = topartists['artist'][0] 
    first_artist_name = first_artist['name'] 
    return first_artist_name # return the top artist in Spain

api_key='d9a77b303d19ede56de6bbf8838cf5d1'
url ='http://ws.audioscrobbler.com/2.0/?method=geo.gettopartists&country=spain&api_key='+api_key+'&format=json'

print(api_get_request(url))