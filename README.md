## Project 1:
Opinion Mining Twitter Tweets
	
# Project Goals: Determine the main topics and build an opinion mining/sentiment model to classify new tweets from Twitter with their related sentiments. Display a few data visualizations with Power BI. 

# GitHub repo (in personal GitHub account)
		○ Status? 
			- Done creating repo and adding collaborators. 
			- https://github.com/devanshithakar12/Twitter-OpinionMining
		
# Design Project Plan
		○ Objectives:
			1. Build a sentiment model using a labelled dataset https://www.kaggle.com/kazanova/sentiment140
				-  Backup Plan:  use TA sentiment analysis API and opinion mining aspect based sentiment analysis feature  https://docs.microsoft.com/en-us/azure/cognitive-services/text-analytics/how-tos/text-analytics-how-to-sentiment-analysis?tabs=version-3-1#opinion-mining)
			2. Use AzureML to train and test model
			3. Choose the best one and deploy with given endpoint
			4. Be able to classify sentiment of new tweets
			5. Display results with some data visualizations using PowerBI
			6.  If time:
				- Apply BOW with TF-IDF and Word2Vec on data
				- Use LDA for topic modeling (gensim LDA package)
					- Once I define the # of topics, I can find the top words for those topics as well as what % of each of the # of topics shows up in that tweet
				
		○ Define Output and success metric:
			- Able to accurately predict and classify sentiment for new tweets from Twitter
			- Visualizations with PowerBI
			
		○ Data Access and description:
			- Use existing labelled dataset for general domain: 
				- https://www.kaggle.com/kazanova/sentiment140 : 1,600,000 tweets assigned a number 0 or 4. 0 is negative, and 4 is positive 
		○ Modeling technique:
			- Own custom sentiment model 
			- AzureML 
			- If time:
				- BOW with TF-IDF
				- Word2Vec
			
		○ Execution stages:
			1. Create a Twitter Developer Account to access tweets
			2. Use labelled dataset with sentiments: https://www.kaggle.com/kazanova/sentiment140
			3. Data Processing/Cleaning (NLTK or Spark Mllib and Spark NLP)
				i. convert data to lowercase 
				ii. replace "RT" (retweet) ,(@ mentions), and non-word characters with blank spaces
				iii. tokenize 
				iv. stem
				v. lemmatize 
				vi. stop word removal  
			4. Store .csv file in Azure Blob Storage
			5. Build a custom sentiment model (or use cogsvcs API for sentiment)
				i. Use AzureML to train, find best one, and deploy with endpoint 
				ii. Pull new tweets from Twitter 
				iii. test and see if model can predict sentiment for new tweet  
			6. Perform LDA to find a certain number of topics 
			
		○ Software Frameworks (tensorflow, keras, nltk, etc.):
			§ Python
			§ NLTK
			§ AzureML
			§ PowerBI
		
Project Architecture Design
		○ Samples
		
Post project write-up (If to be published)
		○ Outline:
		○ Article body:
