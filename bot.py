import praw
import requests
import re

reddit = praw.Reddit(client_id='xxxxxxxxxxxx',
                 	client_secret='xxxxxxxxxxxx',
                 	user_agent='Postcard Lurker Bot 1.0')

# Gets the top-level comment stream from /r/all
for comment in reddit.subreddit('all').stream.comments():

# Uses regular expressions to filter for comments with "postcard"
	if re.search("postcard", comment.body, re.IGNORECASE):
  
# Prints the comment body just so I can verify it's working in the console
		print(comment.body)
		
# Defines the reddit strings as variables
		title = str("Working on it.")
		text = str(comment.body)
		search = str("Comment")
		score = str(comment.score)
		username = str(comment.author)
		subreddit = str("Working on it.")
		category = str("all")
		link = str("https://www.reddit.com" + comment.permalink)
    
# Sets a payload of the Reddit variables to be posted to Google Forms
		payload = {'usp': 'pp_url', 'entry.2139724896': username, 'entry.63049066': search, 'entry.731986394': title, 'entry.1523728882': text, 'entry.2061775572': score, 'entry.689001946': subreddit, 'entry.792247825': category, 'entry.1902202856': link}
   	 	
# Posts to the Google Form with the payload set above as its parameters
		r = requests.post('https://docs.google.com/forms/d/e/xxxxxxxxxxxx/formResponse', params=payload)

for submission in reddit.subreddit('all').stream.submissions():
	try:
		if re.search("postcard", submission.selftext, re.IGNORECASE):
			title = str(submission.title)
			text = str(submission.selftext)
			search = str("Post Text")
			score = str(submission.score)
			username = str(submission.author)
			subreddit = str(submission.subreddit)
			category = str("all")
			link = str("https://www.reddit.com" + submission.permalink)
   	 
			payload = {'usp': 'pp_url', 'entry.2139724896': username, 'entry.63049066': search, 'entry.731986394': title, 'entry.1523728882': text, 'entry.2061775572': score, 'entry.689001946': subreddit, 'entry.792247825': category, 'entry.1902202856': link}
   	 
			r = requests.post('https://docs.google.com/forms/d/e/xxxxxxxxxxxx/formResponse', params=payload)

		if re.search("postcard", submission.title, re.IGNORECASE):
			title = str(submission.title)
			text = str(submission.selftext)
			search = str("Post Title")
    			score = str(submission.score)
			username = str(submission.author)
			subreddit = str(submission.subreddit)
			category = str("all")
			link = str("https://www.reddit.com" + submission.permalink)
   	 
			payload = {'usp': 'pp_url', 'entry.2139724896': username, 'entry.63049066': search, 'entry.731986394': title, 'entry.1523728882': text, 'entry.2061775572': score, 'entry.689001946': subreddit, 'entry.792247825': category, 'entry.1902202856': link}
   	 
			r = requests.post('https://docs.google.com/forms/d/e/xxxxxxxxxxxx/formResponse', params=payload)
