from nltk.tag import StanfordNERTagger

st = StanfordNERTagger(r'F:\Projects\chinesechess\00\AI_MAKER_ChineseChess\stanford-ner-4.2.0\stanford-ner-2020-11-17\classifiers\english.all.3class.distsim.crf.ser.gz') 

res=st.tag('Tom sam David Henry Antonio LionelMessi'.split())

print(res)



# ```
# 斯坦福命名实体识别（Stanford NER）是一个用Java实现的命名实体识别器。命名实体识别（NER）是在文本中标记出表示事物的词语序列的过程，如人名、公司名、基因名、蛋白质名等。

# 斯坦福NER的特点：

# 功能强大的特征提取器：它配备了为命名实体识别精心设计的特征提取器，并提供了许多定义特征提取器的选项。
# 多语言支持：除了为英语提供了优秀的命名实体识别器（特别是针对PERSON、ORGANIZATION、LOCATION这三类）外，还提供了针对不同语言和情境的其他模型，包括仅使用CoNLL 2003英语训练数据训练的模型。
# 通用性：斯坦福NER也被称为CRFClassifier。该软件提供了线性链条件随机场（CRF）序列模型的通用实现。通过在有标签的数据上训练自己的模型，你可以使用此代码为NER或其他任何任务构建序列模型。
# 开源与许可：斯坦福NER是开源的，并遵循GNU通用公共许可证（v2或更高版本）。它包含源代码，并提供命令行调用、作为服务器运行和Java API等多种组件。
# 贡献者：

# 原始的CRF代码由Jenny Finkel编写。
# 特征提取器由Dan Klein、Christopher Manning和Jenny Finkel共同开发。
# 大部分文档和可用性改进归功于Anna Rafferty。
# 最近的代码开发由斯坦福NLP组的多个成员完成。
# 总之，斯坦福NER是一个功能强大、多语言支持且开源的命名实体识别工具，广泛应用于自然语言处理领域。

# ```
