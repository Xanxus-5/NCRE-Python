import jieba

excludes = {"什么", "一个", "我们", "那里", "你们", "如今", 
    "说道", "知道", "老太太", "起来", "姑娘", "这里", "出来",
    "他们", "众人", "自己", "一面", "太太", "只见", "怎么",
    "奶奶", "两个", "没有", "不是", "不知", "这个", "听见"}
f = open("红楼梦.txt", "r")
txt = f.read()
f.close()
words = jieba.lcut(txt)
counts = {}

for word in words :
    if len(word) == 1 :
        continue
    else :
        counts[word] = counts.get(word, 0) + 1

for word in excludes :
    del(counts[word])

items = list(counts.items())
items.sort(key = lambda x:x[1], reverse = True)

for i in range(5) :
    word, count = items[i]
    print("{0:<10} {1:>5}".format(word, count))