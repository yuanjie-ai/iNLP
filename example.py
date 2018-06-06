# -*- coding: utf-8 -*-
"""
__title__ = 'example'
__author__ = 'JieYuan'
__mtime__ = '2018/6/5'
"""
from inlp.convert import char, chinese
from inlp.explode import Strokes, Chars
from inlp.similarity import simhash, thesaurus

print('\n%s\n' % 'inlp.convert')
print(char.half2full("0123456789"))
print(char.full2half("０１２３４５６７８９"))
print(chinese.s2t('忧郁的台湾乌龟')) # chinese.simple2tradition('忧郁的台湾乌龟')
print(chinese.t2s('憂郁的臺灣烏龜')) # chinese.tradition2simple('憂郁的臺灣烏龜')

print('\n%s\n' % 'inlp.explode')
print(Chars().get_chars('袁'))
print(Strokes().get_strokes('袁'))

print('\n%s\n' % 'inlp.similarity')
s1 = ['周杰伦', '是', '一个', '歌手']
s2 = ['刘若英', '是', '个', '演员']
print(simhash(s1, s2))
print(thesaurus.cilin(s1, s2))
print(thesaurus.hownet(s1, s2))