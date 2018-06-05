# -*- coding: utf-8 -*-
"""
__title__ = 'main'
__author__ = 'JieYuan'
__mtime__ = '2018/6/5'
"""

'''
混合采用词林和知网的相似度计算方法。得到更加符合人们感觉的相似度数值
'''

from .cilin.V3.ciLin import CilinSimilarity
from .hownet.howNet import How_Similarity


class Similarity(object):
    def __init__(self):
        self.how_net = How_Similarity()
        self.ci_lin = CilinSimilarity()
        self.Common = self.ci_lin.vocab & self.how_net.vocab
        self.A = self.how_net.vocab - self.ci_lin.vocab
        self.B = self.ci_lin.vocab - self.how_net.vocab

    def ensmble(self, w1, w2):
        '''
        -1表示未收录
        '''
        lin = self.ci_lin.sim2018(w1, w2) if w1 in self.ci_lin.vocab and w2 in self.ci_lin.vocab else 0
        how = self.how_net.calc(w1, w2) if w1 in self.how_net.vocab and w2 in self.how_net.vocab else 0

        if w1 in self.Common and w2 in self.Common:  # 两个词都被词林和知网共同收录。
            print('两个词被词林和知网共同收录')
            print('词林相似度：', lin)
            print('知网相似度：', how)
            return lin * 1 + how * 0  # 可以调节两者的权重，以获取更优结果！！

        if w1 in self.A and w2 in self.A:  # 两个词都只被知网收录。
            return how
        if w1 in self.B and w2 in self.B:  # 两个词都只被词林收录。
            return lin

        if w1 in self.A and w2 in self.B:  # 一个只被词林收录，另一个只被知网收录。
            print('触发策略三，左词为知网，右词为词林')
            same_words = self.ci_lin.code_word[self.ci_lin.word_code[w2][0]]
            if not same_words:
                return 0.2
            all_sims = [self.how_net.calc(word, w1) for word in same_words]
            print(same_words, all_sims)
            return max(all_sims)

        if w2 in self.A and w1 in self.B:
            print('触发策略三，左词为词林，右词为知网')
            same_words = self.ci_lin.code_word[self.ci_lin.word_code[w1][0]]
            if not same_words:
                return 0.2
            all_sims = [self.how_net.calc(word, w2) for word in same_words]
            print(w1, '词林同义词有：', same_words, all_sims)
            return max(all_sims)

        if w1 in self.A and w2 in self.Common:
            print('策略四（左知网）：知网相似度结果为：', how)
            same_words = self.ci_lin.code_word[self.ci_lin.word_code[w2][0]]
            if not same_words:
                return how
            all_sims = [self.how_net.calc(word, w1) for word in same_words]
            print(w2, '词林同义词有：', same_words, all_sims)
            return 0.6 * how + 0.4 * max(all_sims)

        if w2 in self.A and w1 in self.Common:
            print('策略四（右知网）：知网相似度结果为：', how)
            same_words = self.ci_lin.code_word[self.ci_lin.word_code[w1][0]]
            if not same_words:
                return how
            all_sims = [self.how_net.calc(word, w2) for word in same_words]
            print(same_words, all_sims)
            return 0.6 * how + 0.4 * max(all_sims)

        if w1 in self.B and w2 in self.Common:
            print(w1, w2, '策略五（左词林）：词林改进版相似度：', lin)
            same_words = self.ci_lin.code_word[self.ci_lin.word_code[w1][0]]
            if not same_words:
                return lin
            all_sims = [self.how_net.calc(word, w2) for word in same_words]
            print(w1, '词林同义词有：', same_words, all_sims)
            return 0.6 * lin + 0.4 * max(all_sims)

        if w2 in self.B and w1 in self.Common:

            print(w1, w2, '策略五（右词林）：词林改进版相似度：', lin)

            same_words = self.ci_lin.code_word[self.ci_lin.word_code[w2][0]]
            if not same_words:
                return lin
            all_sims = [self.how_net.calc(word, w1) for word in same_words]
            print(w2, '词林同义词有：', same_words, all_sims)
            return 0.6 * lin + 0.4 * max(all_sims)
        return -1


__s = Similarity()
similarity_cilin = __s.ci_lin.sim2018
similarity_hownet = __s.how_net.calc
similarity = Similarity().ensmble

if __name__ == '__main__':
    # 30个  评测词对中的左侧词
    MC30_A = ['轿车', '宝石', '旅游', '男孩子', '海岸', '庇护所', '魔术师', '中午', '火炉', '食物', '鸟']
    # 30个  评测词对中的右侧词
    MC30_B = ['汽车', '宝物', '游历', '小伙子', '海滨', '精神病院', '巫师', '正午', '炉灶', '水果', '公鸡']
    for i in zip(MC30_A, MC30_B):
        print(similarity(*i))
        print(similarity_cilin(*i))
        print(similarity_hownet(*i))
        print('\n==================\n')

