import re
import requests
from htmldom import htmldom

url = 'https://dantri.com.vn/xa-hoi/vu-xe-khach-tong-rao-chan-duong-sat-tai-xe-dang-bi-treo-bang-20180823162346704.htm'
url2 = 'http://dantri.com.vn/xa-hoi/khoi-to-bat-tam-giam-thuyen-truong-tau-thao-van-2-20160607212256874.htm'
url3 = 'https://dantri.com.vn/xa-hoi/tai-nan-giao-thong-tham-hoa-cua-toan-xa-hoi-1416340290.htm'

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
		contents = dom.find("#divNewsContent > p")
		allContent = []
		# signName = contents.last().text()
		for content in contents:
			text = content.text()
			# if text == signName:
			# 	continue
			allContent.append(text)
		return " ".join(allContent)

	def getTag(dom):
		tags = dom.find("span.news-tags-item > a")
		tagContent = []
		for tag in tags:
			tagContent.append(tag.text())
		return tagContent

content = requests.get(url3)
dom = htmldom.HtmlDom().createDom(content.text)
print("Name     : ", Dantri.getName(dom))
print("Main idea: ", Dantri.getMainIdea(dom))
print("Suggest  : ", Dantri.getSuggest(dom))
print("Content  : ", Dantri.getContent(dom))
print("Tag      : ", Dantri.getTag(dom))

url = 'https://www.24h.com.vn/tin-tuc-trong-ngay/clip-me-dung-xe-khong-tat-may-con-nho-van-ga-dam-vao-goc-cay-c46a856093.html'
url2 = 'https://www.24h.com.vn/tin-tuc-trong-ngay/nu-tai-xe-phong-o-to-nguoc-chieu-len-cau-vuot-va-cai-ket-khong-ngo-c46a931486.html'

class TwentyFourHours:
	def getName(dom):
		return dom.find("h1.bld").text()

	def getMainIdea(dom):
		return dom.find("h2.ctTp").text()

	def getSuggest(dom):
		return []

	def getContent(dom):
		contentList = []
		# contents = dom.find("div.brkNs p")
		# for content in contents:
		# 	contentList.append(content.text())
		contents = dom.find("div.brkNs p")
		for content in contents:
			contentList.append(content.text())
		return re.sub(r'[\n\t]', '', " ".join(contentList).strip())


	def getTag(dom):
		return []

# content = requests.get(url2)
# dom = htmldom.HtmlDom().createDom(content.text)

# print("Name     : ", TwentyFourHours.getName(dom))
# print("Main idea: ", TwentyFourHours.getMainIdea(dom))
# print("Suggest  : ", TwentyFourHours.getSuggest(dom))
# print("Content  : ", TwentyFourHours.getContent(dom))
# print("Tag      : ", TwentyFourHours.getTag(dom))


