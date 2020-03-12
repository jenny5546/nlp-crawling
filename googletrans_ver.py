import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
from googletrans import Translator
# from translate import Translator
import numpy as np

# translator = Translator(to_lang='en')
translator = Translator()
df = pd.read_excel(r'/Users/jaeeun/Desktop/trans_12.xlsx')
# print(df)
wr = pd.DataFrame({'kr':[],'en':[]})

kor = []
eng = []

for index,row in df.iterrows():
    kor.append(str(row[0]))
    # eng.append(translator.translate(str(row[0])))
    eng.append(translator.translate(str(row[0]), dest='en').text)

append = pd.DataFrame({'kr': kor, 'en': eng})
wr = wr.append(append, ignore_index=True)
print(wr)
writer = ExcelWriter('translated_12.xlsx')
wr.to_excel(writer,'Sheet1',index=False)
writer.save()
