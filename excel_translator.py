import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
# import googletrans
# import subprocess
import numpy as np
from translate import Translator

# def translate_text(text, dest_language="en"):
#     # Used to translate using the googletrans library
#     import json
#     translator = googletrans.Translator()
#     try:
#         translation = translator.translate(text=text, dest=dest_language)
#     except json.decoder.JSONDecodeError:
#         # api call restriction
#         process = subprocess.Popen(["nordvpn", "d"], stdout=subprocess.PIPE)
#         process.wait()
#         process = subprocess.Popen(["nordvpn", "c", "canada"], stdout=subprocess.PIPE)
#         process.wait()
#         return Process_Data.translate_text(text=text, dest_language=dest_language)
#     return translation.text

translator= Translator(to_lang="en")
df = pd.read_excel(r'/Users/jaeeun/Desktop/trans_1.xlsx')
wr = pd.DataFrame({'kr':[],'en':[]})

kor = []
eng = []

for index,row in df.iterrows():
    kor.append(str(row[0]))
    # eng.append(translator.translate(str(row[0]), dest='en').text)
    eng.append(translator.translate(str(row[0])))

append = pd.DataFrame({'kr': kor, 'en': eng})
wr = wr.append(append, ignore_index=True)

writer = ExcelWriter('translated_1.xlsx')
wr.to_excel(writer,'Sheet1',index=False)
writer.save()

