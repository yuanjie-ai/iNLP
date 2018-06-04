# -*- coding: utf-8 -*-

from collections import defaultdict


def __map(path):
    dic = defaultdict(list)
    with open(path) as f:
        for i in f:
            _ = i.strip().split('\t')
            if _[0] not in dic:
                dic.setdefault(_[0], []).append(_[1:])
        return dic


simple = __map('./chaizi/chaizi-jt.txt')
tradition = __map('./chaizi/chaizi-ft.txt')
