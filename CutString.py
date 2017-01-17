#coding:utf-8
# making chinese sentence to a set of words
import jieba
ret = "安安你好今天的天氣真差"
seglist = jieba.cut(ret, cut_all=False)
for p in seglist: print p
