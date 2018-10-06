import re
import requests

list_keywords = []
with open('keyword-list.txt', 'r') as f:
	myre = re.compile(r'\'[^\']*\'')
	list_keywords = myre.findall(f.read())
	for i in range(len(list_keywords)):
		list_keywords[i] = list_keywords[i].replace(' ', '+')
		list_keywords[i] = list_keywords[i].replace('\'', '')
	print(list_keywords)

list_site = []
with open('site-list.txt', 'r') as f:
	myre = re.compile(r'\'[^\']*\'')
	list_site = f.read()
	list_site = list_site.split('\n')
	print(list_site)

setLinks = set()
count_word = 0
for search_key in list_keywords:
	count_word+= 1
	for website in list_site:
		for page_num in range(5):
			search_link = 'https://bing.com/search?format=rss&q=site:' + \
			website + '+' + search_key + '&first=' + str(page_num*10+1)
			if page_num == 0:
				print("-->>>    ", search_link)
			r = requests.get(search_link)
			content = r.text

			myre = re.compile(r'<link>([^<]*)</link>')
			links = myre.findall(content)
			for link in links:
				if link.find('bing.com') != -1 or \
				link.find('microsoft.com') != -1 or \
				len(link) < 80:
					continue
				print(link)
				setLinks.add(link)

	lenSet = len(setLinks)
	print("      -------- ", 'word: ', count_word, '/50', \
		'   len: ', lenSet,'/500', " --------")
	if lenSet >= 500:
		break


with open('list500LinkUncensor.txt', 'w') as f:
	for link in setLinks:
		f.write(link+'\n')
