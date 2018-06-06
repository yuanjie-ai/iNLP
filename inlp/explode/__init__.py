# -*- coding: utf-8 -*-
import json
import re
from collections import defaultdict

from ..utils import _simple_path, _tradition_path, _stroke_path

pattern_chinese = re.compile('[\u4e00-\u9fa5]+')


class Chars(object):
    def __init__(self):
        self.__simple = self.__map(_simple_path)
        self.__tradition = self.__map(_tradition_path)

    def get_chars(self, char):
        assert isinstance(char, str) and len(char) == 1
        if pattern_chinese.findall(char):
            if char in self.__simple:
                chars = self.__simple[char]
            else:
                chars = self.__tradition[char]
            return chars
        else:
            print('请输入单个汉字')
            
    def __map(self, path):
        dic = defaultdict(list)
        with open(path, encoding='utf-8') as f:
            for i in f:
                _ = i.strip().split('\t')
                if _[0] not in dic:
                    dic.setdefault(_[0], []).append(_[1])
            return dic


class Strokes(object):
    def __init__(self):
        self.__path = _stroke_path
        with open(self.__path, encoding='utf-8') as f:
            self.__strokes = json.load(f)

    def get_strokes(self, char):
        assert isinstance(char, str) and len(char) == 1

        if pattern_chinese.findall(char):
            if char in self.__strokes:
                pass
            else:
                try:
                    from .strokes.character_stoke_handian import Stoke
                    self.__strokes[char] = Stoke().get_stoke(char)
                except Exception:
                    from .strokes.character_stoke_handian import Stoke
                    self.__strokes[char] = Stoke().get_stoke(char)
                except:
                    print('Broken network\n')
                else:
                    try:
                        with open(self.__path, 'w', encoding='utf-8') as f:
                            json.dump(self.__strokes, f)
                    except:
                        print('Warning: Permission denied\n')  # Permission denied

            return self.__strokes[char]
        else:
            print('请输入单个汉字')
