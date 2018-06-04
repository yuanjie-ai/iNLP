# -*- coding: utf-8 -*-
FULL2HALF = {i + 0xFEE0: i for i in range(0x21, 0x7F)}
FULL2HALF[0x3000] = 0x20
HALF2FULL = {j: i for i, j in FULL2HALF.items()}


def full2half(s):
    '''
    Convert full-width characters to ASCII counterpart
    '''
    return str(s).translate(FULL2HALF)


def half2full(s):
    '''
    Convert all ASCII characters to the full-width counterpart.
    '''
    return str(s).translate(HALF2FULL)
