
import re

with open('F:\\temporary_file\\python_excel\\cloudera.txt',encoding='utf-8') as c:
    '''抽取文本中的英文部分并小写化，并将空格作为分隔拼接为长字符串'''
    text = ' '.join([word.group().lower() for word in re.finditer('[a-zA-Z]+', c.read())])


from wordcloud import WordCloud
import matplotlib.pyplot as plt


'''从文本中生成词云图'''
wordcloud = WordCloud(scale=20,background_color='white',height=400,width=800).generate(text)
plt.figure(figsize=[12, 10])
plt.imshow(wordcloud)
plt.axis('off')
plt.show()



