from underthesea import pos_tag
import pandas as pd

a = pos_tag('')
b = pd.DataFrame()
c = pd.DataFrame(a, columns=["word", "type"])

print(c)
