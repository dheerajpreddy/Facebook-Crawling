from twython import Twython
import json
from collections import Counter
import time
import matplotlib.pyplot as plt
import collections

APP_KEY = "qiOaRLVPldazXmYmF3IaIQw4L" #Consumer key
APP_SECRET = "FAzcCMF1UUyuNuSeddAA1nDJYPeXm6OhaCD084k1t3BZ0HleCY" #Consumer secret
OAUTH_TOKEN = "717220472623071233-oeDgXLyYdqT92Mi06aaAGV7EtSExfKS" # Access token
OAUTH_TOKEN_SECRET = "tVh6WAqVqJ5Pekb3skPON4OD46dyyBAIGOiWjPkZrtglC" #Access token secret

twitter = Twython(APP_KEY,APP_SECRET,OAUTH_TOKEN,OAUTH_TOKEN_SECRET)

data_bglore1 = twitter.get_user_timeline(screen_name='BlrCityPolice', tweet_mode='extended', count = 10000, since_id='1041219775324536832', max_id = '1048217088173588481')
data_bglore2 = twitter.get_user_timeline(screen_name='BlrCityPolice', tweet_mode='extended', count = 10000, since_id='1035758803189256192', max_id = '1041219775324536832')

dates_bglore = []
index_bglore = []
favorite_bglore = []
retweets_bglore = []
score_bglore = []
count_bglore = 1

for data in data_bglore1:
	creation_date = data['created_at']
	dates_bglore.append(creation_date)
	favorite_bglore.append(data['favorite_count'])
	retweets_bglore.append(data['retweet_count'])
	index_bglore.append(count_bglore)
	count_bglore += 1
for data in data_bglore2:
	creation_date = data['created_at']
	dates_bglore.append(creation_date)
	favorite_bglore.append(data['favorite_count'])
	retweets_bglore.append(data['retweet_count'])
	index_bglore.append(count_bglore)
	count_bglore += 1

for i in range(0, len(favorite_bglore)):
	score_bglore.append(2*favorite_bglore[i]+10*retweets_bglore[i])

dic = {}

for date in dates_bglore:
	date = time.strftime('%Y-%m-%d %H:%M:%S', time.strptime(date, '%a %b %d %H:%M:%S +0000 %Y'))
	day = str(date.split(' ')[0])
	if day in dic:
		dic[day] += 1
	else:
		dic[day] = 1

ordered_dict = collections.OrderedDict(sorted(dic.items()))
x = []
y = []
for key, val in ordered_dict.items():
	x.append(key)
	y.append(val)
fig1 = plt.figure(figsize=(25, 15))
axes = plt.gca()
plt.bar(x, y)
plt.ylabel('Number of tweets')
plt.xlabel('Day')
fig1.savefig('frequency_bglore.png')

ans = 0
for score in score_bglore:
	ans += score

ans = ans/len(score_bglore)

fig4 = plt.figure(figsize=(25, 15))
axes = plt.gca()
plt.bar(index_bglore, score_bglore, label = 'Average score pre tweet = '+str(ans))
plt.ylabel('Number of favorites')
plt.xlabel('Tweet #')
plt.legend()
fig4.savefig('score_bglore.png')


dates_baltimore = []
index_baltimore = []
favorite_baltimore = []
retweets_baltimore = []
score_baltimore = []
count_baltimore = 1

data_baltimore1 = twitter.get_user_timeline(screen_name='BaltimorePolice', tweet_mode='extended', count = 10000, since_id='1041219775324536832', max_id = '1048217088173588481')
data_baltimore2 = twitter.get_user_timeline(screen_name='BaltimorePolice', tweet_mode='extended', count = 10000, since_id='1035758803189256192', max_id = '1041219775324536832')

for data in data_baltimore1:
	creation_date = data['created_at']
	dates_baltimore.append(creation_date)
	favorite_baltimore.append(data['favorite_count'])
	retweets_baltimore.append(data['retweet_count'])
	# replies_baltimore.append(data['reply_count'])
	index_baltimore.append(count_baltimore)
	count_baltimore += 1
for data in data_baltimore2:
	creation_date = data['created_at']
	dates_baltimore.append(creation_date)
	favorite_baltimore.append(data['favorite_count'])
	retweets_baltimore.append(data['retweet_count'])
	# replies_baltimore.append(data['reply_count'])
	index_baltimore.append(count_baltimore)
	count_baltimore += 1

for i in range(0, len(favorite_baltimore)):
	score_baltimore.append(2*favorite_baltimore[i]+10*retweets_baltimore[i])

dic = {}

for date in dates_baltimore:
	date = time.strftime('%Y-%m-%d %H:%M:%S', time.strptime(date, '%a %b %d %H:%M:%S +0000 %Y'))
	day = str(date.split(' ')[0])
	if day in dic:
		dic[day] += 1
	else:
		dic[day] = 1

ordered_dict = collections.OrderedDict(sorted(dic.items()))
x = []
y = []
for key, val in ordered_dict.items():
	x.append(key)
	y.append(val)
fig2 = plt.figure(figsize=(25, 15))
axes = plt.gca()
plt.bar(x, y)
plt.ylabel('Number of tweets')
plt.xlabel('Day')
fig2.savefig('frequency_baltimore.png')

ans = 0
for score in score_baltimore:
	ans += score

ans = ans/len(score_baltimore)

fig3 = plt.figure(figsize=(25, 15))
axes = plt.gca()
plt.bar(index_baltimore, score_baltimore, label='Average score per tweet ='+str(ans))
plt.ylabel('Number of favorites')
plt.xlabel('Tweet #')
plt.legend()
fig3.savefig('score_baltimore.png')
