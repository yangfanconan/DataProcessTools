from nltk.tag import StanfordNERTagger

st = StanfordNERTagger(r'F:\Projects\chinesechess\00\AI_MAKER_ChineseChess\stanford-ner-4.2.0\stanford-ner-2020-11-17\classifiers\english.all.3class.distsim.crf.ser.gz') 

res=st.tag('Tom sam David Henry Antonio LionelMessi'.split())

print(res)
