import json
from tweepy import StreamListener
import sentiment_model as sent

class my_listener(StreamListener):
    def on_data(self, tweet):
        sentim=sent.sentiment_model()
        try:
                tweet_data=(json.loads(tweet))
                tweet=tweet_data['text']
                output = open("/Users/jaychauhan/Twitter_Sentiment_Analysis/output/twitter-out.txt","a")
                output.write(sentim.classify_tweets(tweet))
                output.write('\n')
                output.close()
                return True
        except BaseException as e:
            print("Error on_data: %s" % str(e))
        return True

    def on_error(self, status):
        print(status)
        return True