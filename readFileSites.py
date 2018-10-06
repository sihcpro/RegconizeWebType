
list_site = []
with open('site-list.txt', 'r') as f:
	list_site = f.read()
	list_site = list_site.split('\n')
	print(list_site)
