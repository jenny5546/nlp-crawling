from konlpy.tag import Okt
okt=Okt()
print(okt.morphs("범죄의 성립과 처벌은 행위 시의 법률에 의한다."))

# 출력 결과: ['범죄', '의', '성립', '과', '처벌', '은', '행위', '시', '의', '법률', '에', '의한다', '.']