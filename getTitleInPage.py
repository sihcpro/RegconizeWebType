import re
import requests
from htmldom import htmldom

url = 'https://dantri.com.vn/xa-hoi/vu-xe-khach-tong-rao-chan-duong-sat-tai-xe-dang-bi-treo-bang-20180823162346704.htm'

content = requests.get(url)
dom = htmldom.HtmlDom().createDom(content.text)

class Dantri:
	def getName(dom):
		name = dom.find("h1.fon31").text()
		return name

	def getMainIdea(dom):
		title = dom.find("h2.fon33")
		reTagH2 = r'<.*h2.*>'
		reTagBr = r'<.*br.*>'
		reTagA = r'<a[^?]*</a>'
		reTagSpan = r'<span[^?]*</span>'
		# listRegexTags = [reTagA, reTagH2, reTagBr, reTagSpan]
		# for reTag in listRegexTags:
		# 	title = re.sub(reTag, '', title)
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
		contents = dom.find("div#divNewsContent > p")
		allContent = []
		signName = contents.last().text()
		for content in contents:
			text = content.text()
			if text == signName:
				break
			allContent.append(text)
		return " ".join(allContent).strip()

	def getTag(dom):
		tags = dom.find("span.news-tags-item > a")
		tagContent = []
		for tag in tags:
			tagContent.append(tag.text())
		return tagContent

print("Name     : ", Dantri.getName(dom))
print("Main idea: ", Dantri.getMainIdea(dom))
print("Suggest  : ", Dantri.getSuggest(dom))
print("Content  : ", Dantri.getContent(dom))
print("Tag      : ", Dantri.getTag(dom))

url = 'https://www.24h.com.vn/tin-tuc-trong-ngay/clip-me-dung-xe-khong-tat-may-con-nho-van-ga-dam-vao-goc-cay-c46a856093.html'

content = requests.get(url)
dom = htmldom.HtmlDom().createDom(content.text)

class TwentyFourHours:
	def getName(dom):
		return dom.find("h1.bld").text()

	def getMainIdea(dom):
		return dom.find("h2.ctTp").text()

	def getSuggest(dom):
		return []

	def getContent(dom):
		contents = dom.find("div.brkNs > p")
		# print(contents.html())
		contentList = []
		for content in contents:
			contentList.append(content.text())
		return " ".join(contentList).strip()

	def getTag(dom):
		return []

print("Name     : ", TwentyFourHours.getName(dom))
print("Main idea: ", TwentyFourHours.getMainIdea(dom))
print("Suggest  : ", TwentyFourHours.getSuggest(dom))
print("Content  : ", TwentyFourHours.getContent(dom))
print("Tag      : ", TwentyFourHours.getTag(dom))


