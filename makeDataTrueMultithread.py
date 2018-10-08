import os
import re
import time
import _thread
import pandas as pd
from underthesea import pos_tag



getDataTrue = False

global pathSaveFile
# content True
pathOpenFile = "content/true/"
pathSaveFile = "data/true"

# content False
if not getDataTrue:
	pathOpenFile = "content/false/"
	pathSaveFile = "data/false/"






global threadCount
threadCount = []

def makeFile(linkFile):
	with open(pathOpenFile + linkFile, "r") as f:
		content = f.read()

		content = re.sub(r'&\w+;|&#\d+;', ' ', content)
		content = re.sub(r'[^\w,.()?!]{2,}', ' ', content)
		content = re.sub(r'([\d]+(\D[\d]+)*)', ' ', content)

		if len(content) > maxLengContent:
			skipFiles.append(file)
			print("skip!!!")
			threadCount.append("")
			return
		a = pos_tag(content)

		for word, t in a:
			if t in ["CH", "M", "Ny", "Np"]:
				continue
			if t == "N":
				arrNouns.append(word)
			elif t == "V":
				arrVerbs.append(word)
			else:
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

	with open(pathSaveFile + "noun/" + linkFile, "w") as f:
		tmp = pd.DataFrame([countNouns.keys(), countNouns.values()], index=["word", "times"]).transpose()
		tmp = tmp.sort_values(["times"], ascending=[0])
		f.write("word,times\n")
		for index, word in tmp.iterrows():
			f.write(word["word"] + "," + str(word["times"]) + "\n")

	with open(pathSaveFile + "verb/" + linkFile, "w") as f:
		tmp = pd.DataFrame([countVerbs.keys(), countVerbs.values()], index=["word", "times"]).transpose()
		tmp = tmp.sort_values(["times"], ascending=[0])
		f.write("word,times\n")
		for index, word in tmp.iterrows():
			f.write(word["word"] + "," + str(word["times"]) + "\n")

	with open(pathSaveFile + "other/" + linkFile, "w") as f:
		tmp = pd.DataFrame([countOther.keys(), countOther.values()], index=["word", "times"]).transpose()
		tmp = tmp.sort_values(["times"], ascending=[0])
		f.write("word,times\n")
		for index, word in tmp.iterrows():
			f.write(word["word"] + "," + str(word["times"]) + "\n")

	threadCount.append("")




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
	_thread.start_new_thread(makeFile, (file,))
	while count > 3 + len(threadCount):
		time.sleep(1)

tmp = len(threadCount)
countBreak = 0
tryTime = 30
while( len(threadCount) < maxCount ):
	if tmp == len(threadCount):
		countBreak+= 1
		if countBreak > tryTime:
			break
	else:
		tmp = len(threadCount)
		countBreak = 0
	time.sleep(1)

for file in skipFiles:
	print(file)
