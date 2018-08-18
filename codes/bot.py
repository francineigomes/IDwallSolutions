# -*- coding: utf-8 -*-
"""
Created on Sat Aug 18 14:11:12 2018

@author: francinei
"""
import telepot
import scrapReddit as sReddit

min_ups = 100
max_limit = 10


bot = telepot.Bot("683547744:AAH0MpdLcXPJV6URmeZZP4iJv0UXG4jVIZ8")
# Receiving messages
input_command  = bot.getUpdates() 

# getting chat id
chat_id = input_command[len(input_command)-1]['message']['chat']['id']

msg_received = input_command[len(input_command)-1]['message']['text']
msg_received_list = msg_received.split()

#%%
if msg_received_list[0] in '/NadaPraFazer':
    # get subreddit names 
    subreddit_names = msg_received_list[1].split(';')

for subreddit_name in subreddit_names:
    get_document = sReddit.reddit_list(subreddit_name, min_ups, max_limit)
    bot.sendMessage(chat_id,get_document)
    # print(get_document)
    
#%%