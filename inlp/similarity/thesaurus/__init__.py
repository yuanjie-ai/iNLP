# -*- coding: utf-8 -*-
"""
__title__ = 'main'
__author__ = 'JieYuan'
__mtime__ = '2018/6/5'
"""

from ...utils import _cilin_path, _hownet_path

class SimCilin(object):
    def __init__(self):
        self.cilin_path = _cilin_path
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
        self.semantic_path = _hownet_path
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


cilin = SimCilin().distance
hownet = SimHownet().distance
