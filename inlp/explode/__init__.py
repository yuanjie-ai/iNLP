# -*- coding: utf-8 -*-

import json
from collections import defaultdict

from ..utils import _get_module_path


class Chars(object):
    def __init__(self):
        self.__simple = self.__map(_get_module_path('./chars/chaizi-jt.txt', __file__))
        self.__tradition = self.__map(_get_module_path('./chars/chaizi-ft.txt', __file__))

    def get_chars(self, char):
        assert isinstance(char, str) and len(char) == 1

        if char in self.__simple:
            chars = self.__simple[char]
        else:
            chars = self.__tradition[char]
        return chars

    def __map(self, path):
        dic = defaultdict(list)
        with open(path) as f:
            for i in f:
                _ = i.strip().split('\t')
                if _[0] not in dic:
                    dic.setdefault(_[0], []).append(_[1])
            return dic


class Strokes(object):
    def __init__(self):
        self.__path = _get_module_path('./strokes/strokes.json', __file__)
        with open(self.__path) as f:
            self.__strokes = json.load(f)

    def get_strokes(self, char):
        assert isinstance(char, str) and len(char) == 1

        if char in self.__strokes:
            pass
        else:
            from .strokes.character_stoke_handian import Stoke
            self.__strokes[char] = Stoke().get_stoke(char)
            with open(self.__path, 'w') as f:
                json.dump(self.__strokes, f)

        return self.__strokes[char]
