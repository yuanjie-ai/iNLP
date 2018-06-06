# -*- coding: utf-8 -*-
"""
__title__ = '__init__.py'
__author__ = 'JieYuan'
__mtime__ = '2018/6/5'
"""
import os


def _get_module_path(path, f):
    """

    :param path:
    :param f: __file__
    :return:
    """
    return os.path.normpath(os.path.join(os.getcwd(), os.path.dirname(f), path))


_cilin_path = _get_module_path('../data/cilin2.txt', __file__)
_hownet_path = _get_module_path('../data/hownet.dat', __file__)
_simple_path = _get_module_path('../data/chaizi-jt.txt', __file__)
_tradition_path = _get_module_path('../data/chaizi-ft.txt', __file__)
_stroke_path = _get_module_path('../data/strokes.json', __file__)
