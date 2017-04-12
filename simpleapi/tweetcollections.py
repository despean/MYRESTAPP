import twitter
import json

CONSUMER_KEY = ''
CONSUMER_SECRET = ''
OAUTH_TOKEN = ''
OAUTH_TOKEN_SECRET = ''
WORLD_WOE_ID = 1
US_WOE_ID = 23424977


def tweet_collection(trending):
    auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET, CONSUMER_KEY, CONSUMER_SECRET)
    twitter_api = twitter.Twitter(auth=auth)
    search_results = twitter_api.search.tweets(q='#SyriaStrikes', count=5000)
    statusses = search_results['statuses']
    for _ in range(100):
        try:
            next_results = search_results['search_metadata']['next_results']
        except KeyError:
            break
        kwargs = dict([kv.split('=') for kv in next_results[1:].split('&')])
        search_results = twitter_api.search.tweets(**kwargs)
        statusses += search_results['statuses']
    data = {}
    for status in statusses:
        status = convert_keys_to_string(status)        
        data['id'] = status['id']
        data['username'] = status['user']['name']
        data['text'] = status['text']
        data['source'] = status['source']
        data['profile_image'] = status['user']['profile_image_url']
        data['screen_name'] = status['user']['screen_name']
        insertTrends(data, trending)
        
    print('-------------------Done!!!--------------------')


def convert_keys_to_string(dictionary):
    if not isinstance(dictionary, dict):
        return dictionary
    return dict((str(k), convert_keys_to_string(v)) 
        for k, v in dictionary.items())



def insertTrends(data, trending):
    id = data['id']
    username = data['username']
    text = data['text']
    source = data['source']
    profile_image = data['profile_image']
    screename = data['screen_name']
    
    tweets = trending(id=id, username=username, text=text, source=source, profile_image=profile_image, screen_name=screename)
    tweets.save()
    
    
    
if __name__ == '__main__':
    data = json.loads(tweet_collection())
    print(tweet_collection())

    

