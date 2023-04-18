#使用LDA进行关键词提取
from gensim import corpora, models, similarities
import pandas as pd
import spacy

#读取数据
data = pd.read_csv('test.csv', encoding='utf-8')

nlp = spacy.load("en_core_web_lg")
stopwords = []
with open("stopwords.txt") as f:
    stopwords = f.read().splitlines()

# 对文本进行分词、去除停用词和提取词干
text = '''
"With the development of OLED technology, OLED has a very broad application prospects, can be widely used in a variety of portable, wall-mounted terminal displays, such as mobile phones, PDAs, digital cameras, handheld DVDs, e-books, electronic paper, rollable wall-mounted commercials, bi-hang TVs, notebook computers and other fields.
At present, OLED is still dominated by small-size products, of which mobile phone panels account for about 58% of overall shipments, which is the most important application; Followed by MP4 players, accounting for about 31%, that is, mobile phones and MP4 two major applications include nearly 90% of OLED panels; The third largest application is car audio accounting for 4%; The proportion of other applications such as TVs, digital cameras, and game consoles is still light, so the first step in the large-scale commercialization of OLED is to start from the two major areas of mobile phones and MP3 players. According to the latest research report published by market research company Display Search, the current global OLED market size is 80 billion yuan, and China's annual OLED shipments in 2021 are 587 million pieces, an increase of 12 times compared with 0.47 billion pieces in 2016, and the market share exceeds 30 billion yuan.","1."
'''
doc = nlp(text)
lemmas = []
pos = []
for token in doc:
    if not token.is_stop:
        lemma = token.lemma_.lower().strip()
        if lemma and lemma not in stopwords:
            lemmas.append(lemma)
            pos.append(token.pos_)
p_list = ['NOUN','ADJ','ADV','NOUN']
for (index,p) in enumerate(pos):
    if p in p_list:
        print(lemmas[index])

