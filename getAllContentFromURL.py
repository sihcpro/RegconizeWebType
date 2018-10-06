import re
import requests
import _thread
from htmldom import htmldom

class Dantri:
	def getName(dom):
		name = dom.find("h1.fon31").text()
		return name

	def getMainIdea(dom):
		title = dom.find("h2.fon33")
		a = title.children()
		title = re.sub(r'<a[^?]*</a>', '', title.text())
		for i in a:
			# print(i.text())
			title = title.replace(i.text(), "")
		return title.strip()

	def getSuggest(dom):
		suggests = dom.find("h2.fon33 > a")
		suggestContent = []
		for suggest in suggests:
			suggestContent.append(suggest.text())
		return suggestContent

	def getContent(dom):
		contents = dom.find("#divNewsContent p")
		allContent = []
		signName = contents.last().text()
		for content in contents:
			text = content.text()
			if text == signName:
				continue
			allContent.append(text)
		return " ".join(allContent)

	def getTag(dom):
		tags = dom.find("span.news-tags-item > a")
		tagContent = []
		for tag in tags:
			tagContent.append(tag.text())
		return tagContent

class TwentyFourHours:
	def getName(dom):
		return dom.find("h1.bld").text()

	def getMainIdea(dom):
		return dom.find("h2.ctTp").text()

	def getSuggest(dom):
		return []

	def getContent(dom):
		contentList = []
		contents = dom.find("div.brkNs p")
		for content in contents:
			content = re.sub(r'<[^<]*>', ' ', content.html())
			contentList.append(content)
		return re.sub(r'[\n\t]', ' ', " ".join(contentList).strip())

	def getTag(dom):
		return []








list_URL = []
with open('list500LinkUncensor.txt', 'r') as f:
	list_URL = f.read()
	list_URL = list_URL.split('\n')
	# print(list_site)

def getInfoDantri(fileName, dom):
	# a = Dantri.getName(dom)
	# b = Dantri.getMainIdea(dom)
	# c = Dantri.getContent(dom)
	# print("Name     : ", a)
	# print("Main idea: ", b)
	# print("Content  : ", c)
	with open("content/"+fileName, "w") as f:
		f.write(Dantri.getName(dom))
		f.write("\n")
		f.write(Dantri.getMainIdea(dom))
		f.write("\n")
		f.write(Dantri.getContent(dom))

def getInfoTwentyFourHours(fileName, dom):
	# a = TwentyFourHours.getName(dom)
	# b = TwentyFourHours.getMainIdea(dom)
	# c = TwentyFourHours.getContent(dom)
	# print("Name     : ", a)
	# print("Main idea: ", b)
	# print("Content  : ", c)
	with open("content/"+fileName, "w") as f:
		f.write(TwentyFourHours.getName(dom))
		f.write("\n")
		f.write(TwentyFourHours.getMainIdea(dom))
		f.write("\n")
		f.write(TwentyFourHours.getContent(dom))


for url in list_URL:
	if len(url) < 70:
		continue
	fileName = re.compile(r'([^/]*$)').findall(url)[0]
	if len(fileName) == 0:
		print("!!!            No name!")
		fileName = url
	dom = htmldom.HtmlDom().createDom(requests.get(url).text)
	print("---> link: ", url)
	if url.find("dantri") != -1:
		# _thread.start_new_thread( getInfoDantri, (fileName, dom))
		next
	else:
		_thread.start_new_thread( getInfoTwentyFourHours, (fileName, dom))
		# input()
