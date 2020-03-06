import MeCab
import nltk

m = MeCab.Tagger()
out = m.parse("(범죄의 성립과 처벌)범죄의 성립과 처벌은 행위 시의 법률에 의한다.")
# print(out)
def pos_tagger(s):
    """ (단어,태그) 셋을 만들기 """
    word_tag = []
    for r in s.split('\n'):
        p = r.split('\t')
        if len(p) > 1:
            w, o = p
            t = o.split(',')[0]
            word_tag.append((w,t))
    return word_tag
set_wp = pos_tagger(out)
print(set_wp)

# [('(', '名詞'), ('범죄의', '記号'), ('성립과', '記号'), ('처벌', '記号'), 
# (')', '名詞'), ('범죄의', '記号'), ('성립과', '記号'), ('처벌은', '記号'), 
# ('행위', '記号'), ('시의', '記号'), ('법률에', '記号'), ('의한다', '記号'), ('.', '名詞')]


grammar = """
명사: {<NNG>}
명사구: {<명사><JKG><명사>}
"""
# Define a chunk grammar, or chunking rules, then chunk
grammar = """
NP: {<N.*>*<Suffix>?}   # Noun phrase
VP: {<V.*>*}            # Verb phrase
AP: {<A.*>*}            # Adjective phrase
"""
parser = nltk.RegexpParser(grammar)
chunks = parser.parse(set_wp)
print("# Print whole tree")
print(chunks.pprint())
# Print whole tree
# (S
#   (/名詞
#   범죄의/記号
#   성립과/記号
#   처벌/記号
#   )/名詞
#   범죄의/記号
#   성립과/記号
#   처벌은/記号
#   행위/記号
#   시의/記号
#   법률에/記号
#   의한다/記号
#   ./名詞)
# None


