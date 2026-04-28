# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 12:01:19 2026

@author: PC41
"""

def tabuada():
    n=1
    while n<11:
        for i in range (1,11):
            print(f"{n} x {i} = {n*i}")
        n+=1

tabuada()