# -*- coding: utf-8 -*-
"""
Created on Sat Aug 18 15:46:25 2018

@author: francinei
"""
#%%
import praw as pw

def reddit_list(subreddit_name, min_ups = 5000, max_limit = 100):
    top_reddits = ''
    reddit = pw.Reddit(client_id ='CEboIpUGujJjuw',
    					 client_secret ='W6dWLRIxx0qKvx18xgi6FvXYZsE', 
    					 password = '270699sf',
    					 user_agent = 'testing script',
    					 username = 'francineigomes')
    m = 50
    subreddit = reddit.subreddit(subreddit_name)
    print(m*'=','\n')
    hot_python = subreddit.hot(limit = max_limit)
    for submission in hot_python:
        if submission.ups > min_ups:
            s_A = 'upvotes:{} \nsubreddit_name:{} \nthread_title:{} \nthread_link:{} \ncomments_links:{}'.format(submission.ups,
                                                                      subreddit_name,
                                                                      submission.title,
                                                                      submission.url,
                                                                      submission.shortlink)
                
            s_B = '\n' + m*'-' +'\n'
            top_reddits = top_reddits + s_A + s_B
    
    return top_reddits
    
    
#%%
