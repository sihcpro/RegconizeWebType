import os
import pandas as pd
from underthesea import pos_tag

listFiles = os.listdir("content")

# allWords = pd.DataFrame()

# listFiles = ['2-xe-o-to-kep-ba-bau-giao-thong-tac-nghen-c46a692241.html']

countNouns = {}
countVerbs = {}
countOther = {}
test = 0
for file in listFiles:
	# test += 1
	# if test > 5:
	# 	break
	with open("content/" + file, "r") as f:
		a = pos_tag(f.read())
		# c = pd.DataFrame(a, columns=["word", "type"])
		# allWords += c
		# print("data : ", c)
		# print("data[noun] : ", c.loc[c['type']=='N'])
		for word, t in a:
			if t in ["CH", "M", "Ny", "Np"]:
				continue
			if t == "N":
				if word in countNouns.keys():
					countNouns[word]+= 1
				else:
					countNouns[word]= 1
			elif t == "V":
				if word in countVerbs.keys():
					countVerbs[word]+= 1
				else:
					countVerbs[word]= 1
			else:
				if word in countOther.keys():
					countOther[word]+= 1
				else:
					countOther[word]= 1


with open("data/list-top-nouns.csv", "w") as f:
	tmp = pd.DataFrame([countNouns.keys(), countNouns.values()], index=["word", "times"]).transpose()
	tmp = tmp.sort_values(["times"], ascending=[0])
	f.write("word,times\n")
	for index, word in tmp.iterrows():
		f.write(word["word"] + "," + str(word["times"]) + "\n")

with open("data/list-top-verbs.csv", "w") as f:
	tmp = pd.DataFrame([countVerbs.keys(), countVerbs.values()], index=["word", "times"]).transpose()
	tmp = tmp.sort_values(["times"], ascending=[0])
	f.write("word,times\n")
	for index, word in tmp.iterrows():
		f.write(word["word"] + "," + str(word["times"]) + "\n")

with open("data/list-top-other.csv", "w") as f:
	tmp = pd.DataFrame([countOther.keys(), countOther.values()], index=["word", "times"]).transpose()
	tmp = tmp.sort_values(["times"], ascending=[0])
	f.write("word,times\n")
	for index, word in tmp.iterrows():
		f.write(word["word"] + "," + str(word["times"]) + "\n")
