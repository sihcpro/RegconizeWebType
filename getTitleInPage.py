import requests
from htmldom import htmldom

url = 'https://dantri.com.vn/xa-hoi/vu-xe-khach-tong-rao-chan-duong-sat-tai-xe-dang-bi-treo-bang-20180823162346704.htm'
content = requests.get(url)

# print( content.text )
dom = htmldom.HtmlDom().createDom(content.text)

find = "h2.sapo"
elem = dom.find( find )

print( elem.html().encode( 'utf-8').decode('utf-8') )
