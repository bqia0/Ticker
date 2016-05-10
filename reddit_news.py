import requests

world_news_url = 'https://www.reddit.com/r/worldnews/.json?limit=10'
headers = {'User-Agent' : 'ticker machine by /u/1s_subshell'}
world_news = requests.get(world_news_url, headers = headers)
print world_news.json()


