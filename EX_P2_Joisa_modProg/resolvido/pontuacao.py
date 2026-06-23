# -*- coding: utf-8 -*-
"""
Editor Spyder

Este é um arquivo de script temporário.
"""
import string


def semPontuacao(s):
    pont = string.punctuation
    ns = ''
    for c in string:
        if c not in pont:
            ns+=c
    return ns

print(semPontuacao('carãmbólas'))