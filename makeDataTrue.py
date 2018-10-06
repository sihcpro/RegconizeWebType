import os
import pandas as pd
from underthesea import pos_tag

listFiles = os.listdir("content")

for file in listFiles:
	with open("content/" + file, "r") as f:
		a = pos_tag(f.read())
		c = pd.DataFrame(a, columns=["word", "type"])
		print("data : ", c)
		print("data[noun] : ", c.loc[c['type']=='N'])
		input()



