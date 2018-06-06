# -*- coding: utf-8 -*-
from simhash import Simhash


class SimHaming:
    '''利用64位数，计算海明距离'''

    def haming_distance(self, code_s1, code_s2):
        x = (code_s1 ^ code_s2) & ((1 << 64) - 1)
        ans = 0
        while x:
            ans += 1
            x &= x - 1
        return ans

    '''利用相似度计算方式,计算全文编码相似度'''

    def get_similarity(self, a, b):
        if a > b:
            return b / a
        else:
            return a / b

    def get_features(self, s):
        word_list = s
        return word_list

    '''计算两个全文编码的距离'''

    def get_distance(self, code_s1, code_s2):
        return self.haming_distance(code_s1, code_s2)

    '''对全文进行编码'''

    def get_code(self, string):
        return Simhash(self.get_features(string)).value

    '''计算s1与s2之间的距离'''

    def distance(self, s1, s2):
        """
        s = '对全文进行分词,提取全文特征,使用词性将虚词等无关字符去重'
        word_list=[word.word for word in jieba.posseg.cut(s) if word.flag[0] not in ['u','x','w','o','p','c','m','q']]
        s1 = word_list
        s2 = ...
        """
        code_s1 = self.get_code(s1)
        code_s2 = self.get_code(s2)
        similarity = (100 - self.haming_distance(code_s1, code_s2) * 100 / 64) / 100
        return similarity


simhash = SimHaming().distance
