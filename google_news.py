import max7219.led as led
from newspaper import Article
import feedparser

output = ' '
device = led.matrix(cascaded = 4)
device.brightness(1)
rss_feed = 'http://news.google.com/news?cf=all&hl=en&pz=1&ned=us&topic=w&output=rss'
d = feedparser.parse(rss_feed)
#print len(d.entries)
def get_title(link):
    article = Article(link)
    article.download()
    article.parse()
    return article.title

def get_news():
    global output 
    for x in d.entries:
        #print get_title(x.link)

        output = output+get_title(x.link)+'      '

while True:
    get_news()
    for x in xrange(10):
        device.show_message(output)
    
