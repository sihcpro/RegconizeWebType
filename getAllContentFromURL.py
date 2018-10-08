import re
import requests
import _thread
import time
from htmldom import htmldom



getDataTrue = False

# content True
linkGetURL = "list500LinkUncensor(2).txt"
pathSaveFile = "content/true/"

# content False
if not getDataTrue:
	linkGetURL = "list-link-false.txt"
	pathSaveFile = "content/false/"






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
		if len(contents.text()) == 0:
			return ""
		allContent = []
		signName = contents.last().text()
		for content in contents:
			text = content.text()
			if text == signName:
				continue
			allContent.append(text)
		content = " ".join(allContent)
		content = re.sub(r'&\w+;|&#\d+;', ' ', content)
		content = re.sub(r'[^\w,.()?!]{2,}', ' ', content)
		content = re.sub(r'([\d]+(\D[\d]+)*)', ' ', content)
		return content

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
		content = " ".join(contentList).strip()
		content = re.sub(r'&\w+;|&#\d+;', ' ', content)
		content = re.sub(r'[^\w,.()?!]{2,}', ' ', content)
		content = re.sub(r'([\d]+(\D[\d]+)*)', ' ', content)
		return content

	def getTag(dom):
		return []








list_URL = []
with open(linkGetURL, 'r') as f:
	list_URL = f.read()
	list_URL = list_URL.split('\n')
	# print(list_site)

global threadCount
threadCount = []
def getInfoDantri(fileName, url):
	content = requests.get(url).text
	content = re.sub(r'<!--([^-]|-[^-]|--[^>])*-->', ' ', content)
	content = re.sub(r'(<script[^>]*>([^<]|<[^/]|</[^s]|</s[^c]|</sc[^r]|</scr[^i]|</scri[^p]|</scrip[^t]|</script[^>])*</script>)', ' ', content)
	content = re.sub(r'(<style[^>]*>[^<]*</style>)', ' ', content)
	dom = htmldom.HtmlDom().createDom(content)
	# a = Dantri.getName(dom)
	# b = Dantri.getMainIdea(dom)
	# c = Dantri.getContent(dom)
	# print("Name     : ", a)
	# print("Main idea: ", b)
	# print("Content  : ", c)
	with open(pathSaveFile + fileName, "w") as f:
		f.write(Dantri.getName(dom))
		f.write("\n")
		f.write(Dantri.getMainIdea(dom))
		f.write("\n")
		f.write(Dantri.getContent(dom))
	threadCount.append("")
	print(len(threadCount), "/", maxCount)

def getInfoTwentyFourHours(fileName, url):
	content = requests.get(url).text
	content = re.sub(r'<!--([^-]|-[^-]|--[^>])*-->', ' ', content)
	content = re.sub(r'(<script[^>]*>([^<]|<[^/]|</[^s]|</s[^c]|</sc[^r]|</scr[^i]|</scri[^p]|</scrip[^t]|</script[^>])*</script>)', ' ', content)
	content = re.sub(r'(<style[^>]*>[^<]*</style>)', ' ', content)
	dom = htmldom.HtmlDom().createDom(content)

	# a = TwentyFourHours.getName(dom)
	# b = TwentyFourHours.getMainIdea(dom)
	# c = TwentyFourHours.getContent(dom)
	# print("Name     : ", a)
	# print("Main idea: ", b)
	# print("Content  : ", c)
	with open(pathSaveFile + fileName, "w") as f:
		f.write(TwentyFourHours.getName(dom))
		f.write("\n")
		f.write(TwentyFourHours.getMainIdea(dom))
		f.write("\n")
		f.write(TwentyFourHours.getContent(dom))
	threadCount.append("")
	print(len(threadCount), "/", maxCount)

# list_URL = ['https://www.24h.com.vn/tin-tuc-trong-ngay/anh-hien-truong-vu-lat-tau-tham-khoc-khien-nhieu-nguoi-thuong-vong-o-thanh-hoa-c46a962118.html', 'https://www.24h.com.vn/tin-tuc-trong-ngay/anh-hien-truong-vu-lat-tau-tham-khoc-khien-nhieu-nguoi-thuong-vong-o-thanh-hoa-c46a962118.html','https://www.24h.com.vn/tin-tuc-trong-ngay/anh-hien-truong-vu-lat-tau-tham-khoc-khien-nhieu-nguoi-thuong-vong-o-thanh-hoa-c46a962118.html']

count = 0
limit = 355
maxCount = min(limit,len(list_URL))
for url in list_URL:
	count += 1
	if count >= limit:
		break
	if len(url) < 70:
		continue
	fileName = re.compile(r'([^/]*$)').findall(url)[0]
	if len(fileName) == 0:
		print("!!!            No name!")
		fileName = url
	print(count, "/", maxCount, " -> ", url)
	if url.find("dantri") != -1:
		_thread.start_new_thread(getInfoDantri, (fileName, url))
	else:
		_thread.start_new_thread(getInfoTwentyFourHours, (fileName, url))

tmp = len(threadCount)
countBreak = 0
tryTime = 10
while( len(threadCount) < maxCount ):
	if tmp == len(threadCount):
		countBreak+= 1
		if countBreak > tryTime:
			break
	else:
		tmp = len(threadCount)
		countBreak = 0
	time.sleep(1)


