import tweepy
import pandas as pd
import nltk
nltk.download('stopwords')
import re

def dataPreprocessing(text):
    # convert text to lowercase 
    text = str(text).lower()
    # replace "rt" with blank space 
    text = re.sub("rt", '', str(text).strip())
    # replace links with blank space (NOT WORKING)
    text = re.sub("http\\w+", '', str(text).strip())
    text = re.sub("https\\w+", '', str(text).strip())
    # replace "mentions with usernames" with blank space 
    text = re.sub("@\\w+", '', str(text).strip())
    # replace all non-word characters with blank space
    text = re.sub(r'[^\w\s]', '', str(text).strip())

    #remove stopwords


    return text
  

#Twitter Access
auth = tweepy.OAuthHandler( '8OkyPd1W4yy3gf4gwpKB9x4qY','P3389lAYJbOmygf1ez8Vn7DdvZjMX2OrEyPavN4wny8XVGM3J1')
auth.set_access_token('1320796292688179200-47ELE46CzdVMnlWAa2X0wloXdj6oNw','oXz7lrgCVW4WShhJyET1J7fCMK8lOnof2B71BvhBdXzUY')
#Call the Tweepy API
api = tweepy.API(auth,wait_on_rate_limit = True)
# status = api.get_status(id, tweet_mode="extended")
df = pd.DataFrame(columns=['text', 'source', 'https://twitter.com/hashtag/ClimateChange?src=hashtag_click'])
tweets = []
tweet =[]

# rpp= number of tweets to return per page, up to a max of 100
# items() = the limit you want
# Cursor helps with pagination and searching existing tweets instead of live
# todo: how do I get the full tweet text instead of cut off tweets
for tweet in tweepy.Cursor(api.search, q='#ClimateChange', rpp=100, lang="en").items(30):
    tweet = [tweet.text] 
    tweets.append(tweet)

# create a dataframe with original tweets from Twitter as well as preprocessed data
df = pd.DataFrame(tweets)
df.columns = ["Text"]
df["ProcessedText"] = df["Text"].apply(dataPreprocessing) 
print(df)

df.to_csv("climate-change-twitter-data.csv", index=False)