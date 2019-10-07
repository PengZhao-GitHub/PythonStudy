from twython import Twython

CONSUMER_KEY = "qK4BH4N2X7b9kZDrIQCdprXRm"
CONSUMER_SECRET = "bRwYWxkdmvgtIm0JO62cBGom6xb4bn5L0ioPA9aChiGQMR2pzV"

twitter = Twython(CONSUMER_KEY, CONSUMER_SECRET)

for status in twitter.search(q='Trump')["statuses"]:
    user = status["user"]["screen_name"].encode('utf-8')
    text = status["text"].encode('utf-8')
    print user, ":", text
    print
    
    



