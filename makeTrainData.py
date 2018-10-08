import os
import csv
import time
import _thread
import numpy as np
import pandas as pd

pathDataTrue = "data/true/"
pathDataFalse = "data/false/"


global threadCount
threadCount = []

def buildTopWord(pathData, typeData):
	data = pd.DataFrame(columns = ["word", "times"])

	listFiles = os.listdir(pathData + typeData + "/")

	count = 0
	limit = 1000
	maxLengFile = min(limit, len(listFiles))
	for file in listFiles:
		count += 1
		if count > limit:
			break
		print(typeData, ":", count, "/", maxLengFile)
		# print(count, "/", maxLengFile, " -> ", file)
		with open(pathData + typeData + "/" + file) as csvfile:
			tmpReader = csv.reader(csvfile)
			tmpData = pd.DataFrame(list(tmpReader)[1:], columns=["word", "times"])
			data = pd.concat( [data, tmpData], axis=0, ignore_index=True)
			# print(tmpData)
	data["times"] = data["times"].apply(pd.to_numeric)
	data = data.groupby('word').sum()
	data = data.sort_values(["times"], ascending=[0]).reset_index()
	# print(data)
	# print(data.memory_usage(deep=True))
	# print(data.info())
	with open(pathData + "list-top-" + typeData + ".csv", "w") as f:
		for index, word in data.iterrows():
			f.write(word["word"] + "," + str(word["times"]) + "\n")
	threadCount.append("")


_thread.start_new_thread(buildTopWord, (pathDataTrue, "noun"))
_thread.start_new_thread(buildTopWord, (pathDataTrue, "verb"))
_thread.start_new_thread(buildTopWord, (pathDataTrue, "other"))


tmp = len(threadCount)
countBreak = 0
tryTime = 60
maxCount = 3

while( len(threadCount) < maxCount ):
	if tmp == len(threadCount):
		countBreak+= 1
		if countBreak > tryTime:
			break
	else:
		tmp = len(threadCount)
		countBreak = 0
	time.sleep(1)



_thread.start_new_thread(buildTopWord, (pathDataFalse, "noun"))
_thread.start_new_thread(buildTopWord, (pathDataFalse, "verb"))
_thread.start_new_thread(buildTopWord, (pathDataFalse, "other"))


maxCount = 6
while( len(threadCount) < maxCount ):
	if tmp == len(threadCount):
		countBreak+= 1
		if countBreak > tryTime:
			break
	else:
		tmp = len(threadCount)
		countBreak = 0
	time.sleep(1)
