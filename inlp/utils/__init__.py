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