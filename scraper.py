from lxml import html
import requests

d = requests.get('http://www.investopedia.com')
headers = {'User-agent':'Mozilla/5.0'}
tree = html.fromstring(d.content)
dow_change = tree.xpath('//*[@id="dow"]/div[1]/span[2]')
print dow_change
