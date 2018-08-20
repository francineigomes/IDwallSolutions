# -*- coding: utf-8 -*-
"""
Created on Sat Aug 18 14:11:12 2018

@author: francinei
"""
import telepot
import scrapReddit as sReddit

min_ups = 5000
max_limit = 100

bot_token = "683547744:AAH0MpdLcXPJV6URmeZZP4iJv0UXG4jVIZ8"
bot = telepot.Bot(bot_token)

# receiving messages
input_command  = bot.getUpdates() 

# getting chat id
chat_id = input_command[len(input_command)-1]['message']['chat']['id']

# getting message text
msg_received = input_command[len(input_command)-1]['message']['text']
msg_received_list = msg_received.split()

if msg_received_list[0] in '/NadaPraFazer':
    # get subreddit names 
    subreddit_names = msg_received_list[1].split(';')

for subreddit_name in subreddit_names:
    get_document = sReddit.reddit_list(subreddit_name, min_ups, max_limit)
    bot.sendMessage(chat_id,get_document)
 
