# -*- coding: utf-8 -*-
from .langconv import Converter


class Chinese(object):
    def __init__(self):
        pass

    def simple2tradition(self, sentence):
        """
        simple2tradition('忧郁的台湾乌龟') >> 憂郁的臺灣烏龜
        """
        return Converter('zh-hant').convert(sentence)

    def tradition2simple(self, sentence):
        """
        tradition2simple('憂郁的臺灣烏龜') >> 忧郁的台湾乌龟
        """
        return Converter('zh-hans').convert(sentence)

_ = Chinese()
s2t = simple2tradition = _.simple2tradition
t2s = tradition2simple = _.tradition2simple
