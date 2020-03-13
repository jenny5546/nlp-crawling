import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
import goslate
import urllib.request
import numpy as np
import time

# proxy_handler = urllib.request.ProxyHandler({"http" : "http://proxy-domain.name:8080"})
# proxy_opener = urllib.request.build_opener(urllib.request.HTTPHandler(proxy_handler), urllib.request.HTTPSHandler(proxy_handler))
translator = goslate.Goslate()

df = pd.read_excel(r'/Users/jaeeun/Desktop/trans_5.xlsx')
# print(df)
wr = pd.DataFrame({'kr':[],'en':[]})

kor = []
eng = []

for index,row in df.iterrows():
    kor.append(str(row[0]))
    # time.sleep(0.5)
    eng.append(translator.translate(str(row[0]), 'en'))
    # time.sleep(0.2)

append = pd.DataFrame({'kr': kor, 'en': eng})
wr = wr.append(append, ignore_index=True)

writer = ExcelWriter('translated_5.xlsx')
wr.to_excel(writer,'Sheet1',index=False)
writer.save()
