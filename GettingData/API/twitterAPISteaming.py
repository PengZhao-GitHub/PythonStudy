from twython import TwythonStreamer
from collections import Counter

CONSUMER_KEY = "qK4BH4N2X7b9kZDrIQCdprXRm"
CONSUMER_SECRET = "bRwYWxkdmvgtIm0JO62cBGom6xb4bn5L0ioPA9aChiGQMR2pzV"
TOKEN_KEY = "821948543988482049-AOVAZqNPErbFKkMNpDkE7gTvHZLaVkm"
TOKEN_SECRET = "eY5y1tcVVorK6BhC6cOjtJMBFqktdQ9AhDtd5RN6OOIKx"

tweets = []

class MyStreamer(TwythonStreamer):
    def on_success(self,data):
        if data['lang'] == 'en':
            tweets.append(data)
            print "received tweet #", len(tweets), data
            
        if len(tweets) >= 100:
            self.disconnect()
            
    def on_error(self, status_code, data):
        print status_code, data
        self.disconnect()
        

stream = MyStreamer(CONSUMER_KEY, CONSUMER_SECRET, TOKEN_KEY, TOKEN_SECRET)

stream.statuses.filter(track='Trump')

top_hashtags = Counter(hashtag['text'].lower()
                       for tweet in tweets
                       for hashtag in tweet['entities']['hashtags'])

print top_hashtags.most_common(5)

