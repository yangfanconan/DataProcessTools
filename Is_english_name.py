from nltk.tag import StanfordNERTagger

### 一些初始化过程
#初始化StanfordNERTagger

st = StanfordNERTagger(r'F:\Projects\chinesechess\00\AI_MAKER_ChineseChess\stanford-ner-4.2.0\stanford-ner-2020-11-17\classifiers\english.all.3class.distsim.crf.ser.gz') #换成实际的路径

res=st.tag('Tom sam David Henry Antonio LionelMessi'.split())

print(res)





def is_english_names(text):
    """
    判断给定的字符串是否为英文名字
    """
    # 去掉字符串中的空格
    text=text.replace(' ','')
    # 判断字符串是否为空
    if text==None or text=='' or text==[]:
        return False
    # 判断字符串中是否含有/，如果有则以/分割，后作为两个字符串处理，判断是否为英文名字
    name1=""
    name2=""
    if '/' in text:
        name1,name2=text.split('/')
    else:
        name1=text
    # 将字符串转换为首字母大写，其他小写的形式
    name1=name1.lower().capitalize()
    name2=name2.lower().capitalize()
    # 将名字拼到一起
    name=name1+name2
    # 使用自然语言处理工具对名字进行分词和词性标注
    res=st.tag(name.split())
    # 获取名字的第一个词的词性
    name_tag=res[0][1]
    # 如果名字的第一个词的词性为'PERSON'，则返回True，否则返回False
    if name_tag=='PERSON':
        return True
    else:
        return False

print(is_english_names('TAYLOR/SWIFT'))
