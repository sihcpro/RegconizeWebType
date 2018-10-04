from urllib.request import urlopen, quote

# param_utf8 = param.encode("utf-8")
# param_perc_encoded = quote(param_utf8)
link = "https://bing.com/search?format=rss&q=" + quote('Lật xe khách')
f = urlopen(link)
myfile = f.read()
print(myfile.decode('utf-8'))