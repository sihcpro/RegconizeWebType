from underthesea import pos_tag
import pandas as pd

a = pos_tag('Chợ thịt chó nổi tiếng ở Sài Gòn bị truy quét')
b = pd.DataFrame()
c = pd.DataFrame(a, columns=["word", "type"])

print(c)
