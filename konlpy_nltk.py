import konlpy
import nltk

# POS tag a sentence
sentence = u'제1조(범죄의 성립과 처벌)범죄의 성립과 처벌은 행위 시의 법률에 의한다.'
words = konlpy.tag.Okt().pos(sentence)

# Define a chunk grammar, or chunking rules, then chunk
grammar = """
NP: {<N.*>*<Suffix>?}   # Noun phrase
VP: {<V.*>*}            # Verb phrase
AP: {<A.*>*}            # Adjective phrase
"""
parser = nltk.RegexpParser(grammar)
chunks = parser.parse(words)
print("# Print whole tree")
print(chunks.pprint())
# (S
#   (NP 제/Noun 1조/Number)
#   (/Punctuation
#   (NP 범죄/Noun)
#   의/Josa
#   (NP 성립/Noun)
#   과/Josa
#   (NP 처벌/Noun)
#   )/Punctuation
#   (NP 범죄/Noun)
#   의/Josa
#   (NP 성립/Noun)
#   과/Josa
#   (NP 처벌/Noun)
#   은/Josa
#   (NP 행위/Noun 시/Noun)
#   의/Josa
#   (NP 법률/Noun)
#   에/Josa
#   (AP 의한다/Adjective)
#   ./Punctuation)
# None

print("\n# Print noun phrases only")
for subtree in chunks.subtrees():
    if subtree.label()=='NP':
        print(' '.join((e[0] for e in list(subtree))))
        print(subtree.pprint())
# 제 1조
# (NP 제/Noun 1조/Number)
# None
# 범죄
# (NP 범죄/Noun)
# None
# 성립
# (NP 성립/Noun)
# None
# 처벌
# (NP 처벌/Noun)
# None
# 범죄
# (NP 범죄/Noun)
# None
# 성립
# (NP 성립/Noun)
# None
# 처벌
# (NP 처벌/Noun)
# None
# 행위 시
# (NP 행위/Noun 시/Noun)
# None
# 법률
# (NP 법률/Noun)
# None
# Display the chunk tree
chunks.draw()