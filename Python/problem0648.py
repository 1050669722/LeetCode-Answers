# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 11:03:23 2019

@author: Administrator
"""

class Solution:
    def replaceWords(self, Dict: list, Sentence: str) -> str:
#        d = {}
#        c = d
#        for word in Dict:
#            word = list(word) #word = list(word)
#            word.reverse()
##            print(word)
#            while word:
#                c[word[-1]] = {}
#                if word:
#                    c = c[word[-1]]
#                mark = word.pop() #word.pop(0)
#                if not word:
#                    c[mark] = 'end'
#            c = d
#        return d
        Dict = sorted(Dict, key = lambda x: len(x))
        Dict.reverse()
        print(Dict)
        d = {}
        c = d
        for word in Dict:
            word = list(word) #word = list(word)
            word.reverse()
            length = len(word)
            while word:
#                try:
#                    d[word[-1]] #对于首字母，字典里已经存在该键，跳过这个单词，即首字母重复的，保留短的词根
#                    break
                try:
                    d[word[-1]] #对于首字母，字典里已经存在该键，跳过这个单词，即首字母重复的，保留短的词根
                    if len(word) == length:
#                        d[word[-1]] #对于首字母，字典里已经存在该键，跳过这个单词，即首字母重复的，保留短的词根
                        d[word[-1]] = {}
                        break
                    else:
                        1/0
                except:
                    c[word[-1]] = {}
                    c = c[word[-1]]
                    word.pop() #word.pop(0)
            c = d
#        print(d)
#        return d
        Sentence = Sentence.split(' ')
#        print(Sentence)
        for k in range(len(Sentence)):
            temp = []
            for letter in Sentence[k]:
                try:
#                    print(-1)
                    c[letter]
                    c = c[letter]
                    temp.append(letter)
                    if c == {}:
                        Sentence[k] = ''.join(temp)
                        c = d #字典复位
                        break
                except:
                    c = d #字典复位
                    break#continue# #题意认为这种词根只能出现在单词开头，所以这里用break，而不是continue，不再继续找下去了。
        return ' '.join(Sentence)#Sentence#
                    
    
#class Solution(object):
#    def __init__(self):
#        self.e = 'end'
#        self.dtree = {}
#
#    def replaceWords(self, dict, sentence):
#        self.build_tree(dict)
#        res = [self.replace(word) for word in sentence.split(' ')]
#        return ' '.join(res)
#
#    def replace(self, word):
#        cur = self.dtree
#        for index, char in enumerate(word):
#            if char in cur:
#                cur = cur[char]
#                if self.e in cur:
#                    return word[:index+1]
#            else:
#                return word
#        return word
#
#    # {'b': {'a': {'t': {'end': ''}}}, 'r': {'a': {'t': {'end': ''}}}, 'c': {'a': {'t': {'end': ''}}}}
#    def build_tree(self, dict):
#        for pre in dict:
#            cur = self.dtree
#            for char in pre:
#                if char not in cur:
#                    cur[char] = {}
#                cur = cur[char]
#            cur[self.e] = ''
        
        
solu = Solution()
Dict, Sentence = ["cat", "bat", "rat"], "the cattle was rattled by the battery"
#solu.replaceWords(Dict, Sentence)
Dict, Sentence = ["a", "aa", "aaa", "aaaa"], "a aa a aaaa aaa aaa aaa aaaaaa bbb baba ababa"
Dict, Sentence = ["e","k","c","harqp","h","gsafc","vn","lqp","soy","mr","x","iitgm","sb","oo","spj","gwmly","iu","z","f","ha","vds","v","vpx","fir","t","xo","apifm","tlznm","kkv","nxyud","j","qp","omn","zoxp","mutu","i","nxth","dwuer","sadl","pv","w","mding","mubem","xsmwc","vl","farov","twfmq","ljhmr","q","bbzs","kd","kwc","a","buq","sm","yi","nypa","xwz","si","amqx","iy","eb","qvgt","twy","rf","dc","utt","mxjfu","hm","trz","lzh","lref","qbx","fmemr","gil","go","qggh","uud","trnhf","gels","dfdq","qzkx","qxw"], "ikkbp miszkays wqjferqoxjwvbieyk gvcfldkiavww vhokchxz dvypwyb bxahfzcfanteibiltins ueebf lqhflvwxksi dco kddxmckhvqifbuzkhstp wc ytzzlm gximjuhzfdjuamhsu gdkbmhpnvy ifvifheoxqlbosfww mengfdydekwttkhbzenk wjhmmyltmeufqvcpcxg hthcuovils ldipovluo aiprogn nusquzpmnogtjkklfhta klxvvlvyh nxzgnrveghc mpppfhzjkbucv cqcft uwmahhqradjtf iaaasabqqzmbcig zcpvpyypsmodtoiif qjuiqtfhzcpnmtk yzfragcextvx ivnvgkaqs iplazv jurtsyh gzixfeugj rnukjgtjpim hscyhgoru aledyrmzwhsz xbahcwfwm hzd ygelddphxnbh rvjxtlqfnlmwdoezh zawfkko iwhkcddxgpqtdrjrcv bbfj mhs nenrqfkbf spfpazr wrkjiwyf cw dtd cqibzmuuhukwylrnld dtaxhddidfwqs bgnnoxgyynol hg dijhrrpnwjlju muzzrrsypzgwvblf zbugltrnyzbg hktdviastoireyiqf qvufxgcixvhrjqtna ipfzhuvgo daee r nlipyfszvxlwqw yoq dewpgtcrzausqwhh qzsaobsghgm ichlpsjlsrwzhbyfhm ksenb bqprarpgnyemzwifqzz oai pnqottd nygesjtlpala qmxixtooxtbrzyorn gyvukjpc s mxhlkdaycskj uvwmerplaibeknltuvd ocnn frotscysdyclrc ckcttaceuuxzcghw pxbd oklwhcppuziixpvihihp"
print(solu.replaceWords(Dict, Sentence))
        

