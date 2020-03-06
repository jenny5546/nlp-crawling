import spacy
import pandas as pd
df = pd.read_excel(r'/Users/jaeeun/Desktop/file.xlsx')
nlp = spacy.load("en_core_web_sm")

for index,row in df.iterrows():
    # print(row[0])
    doc = nlp(row[0])
    chunks = []
    for nc in doc.noun_chunks:
        chunks.append(nc.text)
    new = sorted(set(chunks), key=lambda x: chunks.index(x))
    print(new)



