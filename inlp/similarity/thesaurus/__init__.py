# -*- coding: utf-8 -*-
"""
__title__ = 'main'
__author__ = 'JieYuan'
__mtime__ = '2018/6/5'
"""
import os

from .cilin.V3.ciLin import CilinSimilarity
from .hownet.howNet import How_Similarity

_get_module_path = lambda path: os.path.normpath(os.path.join(os.getcwd(), os.path.dirname(__file__), path))


class Similarity(object):
    '''
    混合采用词林和知网的相似度计算方法。得到更加符合人们感觉的相似度数值
    '''

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


class SimCilin(object):
    def __init__(self):
        self.cilin_path = _get_module_path('./cilin/V2/cilin.txt')
        self.sem_dict = self.load_semantic()

    '''加载语义词典'''

    def load_semantic(self):
        sem_dict = {}
        for line in open(self.cilin_path, encoding='utf-8'):
            line = line.strip().split(' ')
            sem_type = line[0]
            words = line[1:]
            for word in words:
                if word not in sem_dict:
                    sem_dict[word] = sem_type
                else:
                    sem_dict[word] += ';' + sem_type

        for word, sem_type in sem_dict.items():
            sem_dict[word] = sem_type.split(';')
        return sem_dict

    '''比较计算词语之间的相似度，取max最大值'''

    def compute_word_sim(self, word1, word2):
        sems_word1 = self.sem_dict.get(word1, [])
        sems_word2 = self.sem_dict.get(word2, [])
        score_list = [self.compute_sem(sem_word1, sem_word2) for sem_word1 in sems_word1 for sem_word2 in sems_word2]
        if score_list:
            return max(score_list)
        else:
            return 0

    '''基于语义计算词语相似度'''

    def compute_sem(self, sem1, sem2):
        sem1 = [sem1[0], sem1[1], sem1[2:4], sem1[4], sem1[5:7], sem1[-1]]
        sem2 = [sem2[0], sem2[1], sem2[2:4], sem2[4], sem2[5:7], sem2[-1]]
        score = 0
        for index in range(len(sem1)):
            if sem1[index] == sem2[index]:
                if index in [0, 1]:
                    score += 3
                elif index == 2:
                    score += 2
                elif index in [3, 4]:
                    score += 1
        return score / 10

    '''基于词相似度计算句子相似度'''

    def distance(self, s1, s2):
        """句子相似度
        :params: ['周杰伦', '是', '一个', '歌手'], ['刘若英', '是', '个', '演员']
        """
        words1 = s1
        words2 = s2
        score_words1 = []
        score_words2 = []
        for word1 in words1:
            score = max(self.compute_word_sim(word1, word2) for word2 in words2)
            score_words1.append(score)
        for word2 in words2:
            score = max(self.compute_word_sim(word2, word1) for word1 in words1)
            score_words2.append(score)
        similarity = max(sum(score_words1) / len(words1), sum(score_words2) / len(words2))

        return similarity


class SimHownet:
    def __init__(self):
        self.semantic_path = _get_module_path('./hownet/hownet.dat')
        self.semantic_dict = self.load_semanticwords()

    '''加载语义词典'''

    def load_semanticwords(self):
        semantic_dict = {}
        for line in open(self.semantic_path, encoding='utf-8'):
            words = [word for word in line.strip().replace(' ', '>').replace('\t', '>').split('>') if word != '']
            word = words[0]
            word_def = words[2]
            semantic_dict[word] = word_def.split(',')
        return semantic_dict

    '''基于语义计算语义相似度'''

    def calculate_semantic(self, DEF1, DEF2):
        DEF_INTERSECTION = set(DEF1).intersection(set(DEF2))
        DEF_UNION = set(DEF1).union(set(DEF2))
        return float(len(DEF_INTERSECTION)) / float(len(DEF_UNION))

    '''比较两个词语之间的相似度'''

    def compute_similarity(self, word1, word2):
        DEFS_word1 = self.semantic_dict.get(word1, [])
        DEFS_word2 = self.semantic_dict.get(word2, [])
        scores = [self.calculate_semantic(DEF_word1, DEF_word2) for DEF_word1 in DEFS_word1 for DEF_word2 in DEFS_word2]
        if scores:
            return max(scores)
        else:
            return 0

    '''基于词语相似度计算句子相似度'''

    def distance(self, s1, s2):
        """句子相似度
        :params: ['周杰伦', '是', '一个', '歌手'], ['刘若英', '是', '个', '演员']
        """
        words1 = s1
        words2 = s2
        score_words1 = []
        score_words2 = []
        for word1 in words1:
            score = max(self.compute_similarity(word1, word2) for word2 in words2)
            score_words1.append(score)
        for word2 in words2:
            score = max(self.compute_similarity(word2, word1) for word1 in words1)
            score_words2.append(score)
        similarity = max(sum(score_words1) / len(words1), sum(score_words2) / len(words2))

        return similarity


# __s = Similarity()
# similarity_cilin = similarity_cilin_w = __s.ci_lin.sim2018
# similarity_hownet = similarity_hownet_w = __s.how_net.calc
# similarity = Similarity().ensmble


cilin = SimCilin().distance
hownet = SimHownet().distance
