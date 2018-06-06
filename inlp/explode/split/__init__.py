# -*- coding: utf-8 -*-

import os
from collections import defaultdict

_get_module_path = lambda path: os.path.normpath(os.path.join(os.getcwd(), os.path.dirname(__file__), path))

def __map(path):
    dic = defaultdict(list)
    with open(path) as f:
        for i in f:
            _ = i.strip().split('\t')
            if _[0] not in dic:
                dic.setdefault(_[0], []).append(_[1]) # _[1:]
        return dic


simple = __map(_get_module_path('./chaizi/chaizi-jt.txt'))
tradition = __map(_get_module_path('./chaizi/chaizi-ft.txt'))
