import max7219.led as led
from newspaper import Article
import feedparser

output = ' '
device = led.matrix(cascaded = 5)
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
        title = get_title(x.link)
        print title
        output = output+ title+ '     '
        #device.show_message(get_title(x.link))
try:
    while True:
        get_news()
        for x in xrange(0,9):
            device.show_message(output)
except IndexError:
    print output
    print "shits fucked up again idiot"
