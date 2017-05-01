# -*- coding: utf-8 -*-
import twitter
import json
import django

CONSUMER_KEY = ''
CONSUMER_SECRET = ''
OAUTH_TOKEN = ''
OAUTH_TOKEN_SECRET = ''
WORLD_WOE_ID = 1
US_WOE_ID = 23424977


def tweet_collection(trending):
    auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET, CONSUMER_KEY, CONSUMER_SECRET)
    twitter_api = twitter.Twitter(auth=auth)
    w_trend = [trend['name'] for trend in twitter_api.trends.place(_id=WORLD_WOE_ID)[0]['trends']]
    for topic in w_trend:

        search_results = twitter_api.search.tweets(q=topic, count=5000)
        statuses = search_results['statuses']
        for _ in range(100):
            try:
                next_results = search_results['search_metadata']['next_results']
            except KeyError:
                break
            kwargs = dict([kv.split('=') for kv in next_results[1:].split('&')])
            search_results = twitter_api.search.tweets(**kwargs)
            statuses += search_results['statuses']
        data = {}
        for status in statuses:
            status = convert_keys_to_string(status)
            data['id'] = status['id']
            data['username'] = status['user']['name']
            data['text'] = status['text']
            data['source'] = status['source']
            data['profile_image'] = status['user']['profile_image_url']
            data['screen_name'] = status['user']['screen_name']
            data['hash_tag'] = topic

            insertTrends(data, trending)
        break


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
    hast_tag = data['hash_tag']
    tweets = trending(tweet_id=id, username=username, text=text, source=source, profile_image=profile_image,screen_name=screename, hash_tag=hast_tag)
    tweets.save()




if __name__ == '__main__':
    data = json.loads(tweet_collection())
    print(tweet_collection())
