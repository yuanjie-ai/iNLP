# -*- coding: utf-8 -*-
"""
__title__ = 'example'
__author__ = 'JieYuan'
__mtime__ = '2018/6/5'
"""

from inlp.explode import Strokes

s = Strokes()

print(s.get_strokes('繁'))

# ['ノ', '一', 'フ', 'フ', '丶', '一', '丶', 'ノ', '一', 'ノ', '丶', 'フ', 'フ', '丶', '丨', 'ノ', '丶']