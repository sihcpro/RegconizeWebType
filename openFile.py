import re

myre = re.compile(r'\'[^\']*\'')

file_object  = open('keyword-list.txt', 'r')
list_content = myre.findall(file_object.read())

print( type(list_content) )

for i in range(len(list_content)):
	list_content[i] = list_content[i].replace(' ', '+')
	list_content[i] = list_content[i].replace('\'', '')

print(list_content)
