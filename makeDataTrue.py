import os
import re
import pandas as pd
from underthesea import pos_tag


getDataTrue = False

# content True
pathOpenFile = "content/true/"
pathSaveFile = "data/true"

# content False
if not getDataTrue:
	pathOpenFile = "content/false/"
	pathSaveFile = "data/false/"





listFiles = os.listdir(pathOpenFile)

skipFiles = []
countNouns = {}
countVerbs = {}
countOther = {}
arrNouns = []
arrVerbs = []
arrOther = []
count = 0
limit = 1000
maxCount = min(limit, len(listFiles))
maxLengContent = 20000

for file in listFiles:
	count += 1
	if count >= limit:
		break
	print(count, "/", maxCount, " -> ", file)
	with open(pathOpenFile + file, "r") as f:
		content = f.read()

		content = re.sub(r'&\w+;|&#\d+;', ' ', content)
		content = re.sub(r'[^\w,.()?!]{2,}', ' ', content)
		content = re.sub(r'([\d]+(\D[\d]+)*)', ' ', content)

		# print(content)
		# print("---------------------------------------------------------------\n\n\n\n\n\n")

		if len(content) > maxLengContent:
			skipFiles.append(file)
			print("skip!!!")
			continue
		a = pos_tag(content)

		# c = pd.DataFrame(a, columns=["word", "type"])
		# allWords += c
		# print("data : ", c)
		# print("data[noun] : ", c.loc[c['type']=='N'])

		for word, t in a:
			if t in ["CH", "M", "Ny", "Np"]:
				continue
			if t == "N":
				# if word in countNouns.keys():
				# 	countNouns[word]+= 1
				# else:
				# 	countNouns[word]= 1
				arrNouns.append(word)
			elif t == "V":
				# if word in countVerbs.keys():
				# 	countVerbs[word]+= 1
				# else:
				# 	countVerbs[word]= 1
				arrVerbs.append(word)
			else:
				# if word in countOther.keys():
				# 	countOther[word]+= 1
				# else:
				# 	countOther[word]= 1
				arrOther.append(word)


for i in arrNouns:
	countNouns[i] = 0
for i in arrNouns:
	countNouns[i] += 1

for i in arrVerbs:
	countVerbs[i] = 0
for i in arrVerbs:
	countVerbs[i] += 1

for i in arrOther:
	countOther[i] = 0
for i in arrOther:
	countOther[i] += 1

with open(pathSaveFile + "list-top-nouns.csv", "w") as f:
	tmp = pd.DataFrame([countNouns.keys(), countNouns.values()], index=["word", "times"]).transpose()
	tmp = tmp.sort_values(["times"], ascending=[0])
	f.write("word,times\n")
	for index, word in tmp.iterrows():
		f.write(word["word"] + "," + str(word["times"]) + "\n")

with open(pathSaveFile + "list-top-verbs.csv", "w") as f:
	tmp = pd.DataFrame([countVerbs.keys(), countVerbs.values()], index=["word", "times"]).transpose()
	tmp = tmp.sort_values(["times"], ascending=[0])
	f.write("word,times\n")
	for index, word in tmp.iterrows():
		f.write(word["word"] + "," + str(word["times"]) + "\n")

with open(pathSaveFile + "list-top-other.csv", "w") as f:
	tmp = pd.DataFrame([countOther.keys(), countOther.values()], index=["word", "times"]).transpose()
	tmp = tmp.sort_values(["times"], ascending=[0])
	f.write("word,times\n")
	for index, word in tmp.iterrows():
		f.write(word["word"] + "," + str(word["times"]) + "\n")

for file in skipFiles:
	print(file)
