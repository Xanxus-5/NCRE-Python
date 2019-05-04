import jieba
from wordcloud import WordCloud 

excludes = {"什么", "一个", "我们", "那里", "你们", "如今", 
    "说道", "知道", "老太太", "起来", "姑娘", "这里", "出来",
    "他们", "众人", "自己", "一面", "太太", "只见", "怎么",
    "奶奶", "两个", "没有", "不是", "不知", "这个", "听见"}
f = open("红楼梦.txt", "r")
txt = f.read()
f.close()
words = jieba.lcut(txt)
newtxt = ''.join(words)
wordcloud = WordCloud(background_color = "white", \
    width = 800, \
    height = 600, \
    font_path = "msyh.ttc", \
    max_words = 200, \
    max_font_size = 80, \
    stopwords = excludes).generate(newtxt)
wordcloud.to_file('红楼梦基本词云.png')