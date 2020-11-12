import tweepy
import pandas as pd
import nltk
nltk.download('stopwords')
import re
import os 
from dotenv import load_dotenv 
# from sklearn.model_selection import train_test_split
# from sklearn import  model_selection
load_dotenv()

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

    # tokenize 
    # tokenized_text = text.split()
    # remove stopwords 
    # tokenized_text = [w for w in tokenized_text if w not in eng_stopwords]
    # text = " ".join(tokenized_text)
    return text
    
oauth_consumer_key = os.getenv('OAUTH_CONSUMER_KEY')
oauth_consumer_secret = os.getenv('OAUTH_CONSUMER_SECRET')
access_token_key = os.getenv('ACCESS_TOKEN_KEY')
access_token_secret = os.getenv('ACCESS_TOKEN_SECRET')

#Twitter Access
auth = tweepy.OAuthHandler( oauth_consumer_key, oauth_consumer_secret)
auth.set_access_token(access_token_key, access_token_secret)
#Call the Tweepy API
api = tweepy.API(auth,wait_on_rate_limit = True)
# status = api.get_status(id, tweet_mode="extended")
df = pd.DataFrame(columns=['text', 'source', 'https://twitter.com/hashtag/ClimateChange?src=hashtag_click'])
tweets = []
tweet =[]
# eng_stopwords = nltk.corpus.stopwords.words("english")
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

# train_data, test_data = model_selection.train_test_split(df, test_size=0.3)
# train_y = train_data["ProcessedText"].values
# test_y = test_data["ProcessedText"].values

df.to_csv("climate-change-twitter-data.csv", index=False)