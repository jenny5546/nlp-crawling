import spacy
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
import numpy as np

df = pd.read_excel(r'/Users/jaeeun/Desktop/file.xlsx')
nlp = spacy.load("en_core_web_sm")
wr = pd.DataFrame({'a':[],'b':[]})

for index,row in df.iterrows():

    doc = nlp(row[0])
    chunks = []

    for nc in doc.noun_chunks:
        chunks.append(nc.text)

    new = sorted(set(chunks), key=lambda x: chunks.index(x))
    docs =[str(doc)]*len(new)
    print(docs)
    wr2 = pd.DataFrame({'a': new, 'b': docs})
    wr = wr.append(wr2, ignore_index=True)
    print(wr)
    writer = ExcelWriter('coverted.xlsx')
    wr.to_excel(writer,'Sheet1',index=False)
    writer.save()



