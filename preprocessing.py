import jieba


# def stopwordslist(filepath):
#     stopwords = [line.strip() for line in
#                  open(filepath, 'r', encoding='utf-8').readlines()]  # 分别读取停用词表里的每一个词，因为停用词表里的布局是一个词一行
#     return stopwords  # 返回一个列表，里面的元素是一个个的停用词
#
#
# def cutsentences(sentences):  # 定义函数实现分词
#     # print('原句子为：' + sentences)
#     cutsentence = jieba.lcut(sentences.strip())  # 精确模式
#     # print('\n' + '分词后：' + "/ ".join(cutsentence))
#     stopwords = stopwordslist(filepath)  # 这里加载停用词的路径
#     lastsentences = ''
#     for word in cutsentence:  # for循环遍历分词后的每个词语
#         if word not in stopwords:  # 判断分词后的词语是否在停用词表内
#             if word != '\t':
#                 lastsentences += word
#                 # lastsentences += "/ "
#     # print('\n' + '去除停用词后：' + lastsentences)
#     return lastsentences


with open("result.txt", "r", encoding='utf-8') as f:
    data = f.readlines()
    print(data)

# filepath = 'D:\\KG\\ch-NER\\1-my\\data\\stopword1.txt'
# sentences = '万里长城是中国古代劳动人民血汗的结晶和中国古代文化的象征和中华民族的骄傲'
# stopwordslist(filepath)
# cutsentences(sentences)

sent = []
for i in range(len(data)):
    sent.append(data[i])
    with open("result1.txt", "a") as f:
        f.write(data[i])
        f.write("\n")

print(sent)
