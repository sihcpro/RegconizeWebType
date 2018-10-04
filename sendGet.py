import requests
import re

r = requests.get('https://bing.com/search?format=rss&q=Lật+xe+khách')
content = r.text

myre = re.compile(r'<link>([^<]*)</link>')
link = myre.findall(content)

print(link)
