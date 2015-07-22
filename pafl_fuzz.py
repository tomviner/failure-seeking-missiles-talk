import afl
import os
import sys

afl.start()

inp = sys.stdin.read()
inp += '1234'

def f0(ch):
    return ch == 'f'
def f1(ch):
    return ch == 'o'
def f2(ch):
    return ch == 'o'
def f3(ch):
    return ch == '!'

if f0(inp[0]):
    if f1(inp[1]):
        if f2(inp[2]):
            if f3(inp[3]):
    # if inp[1] == 'o':
    #     if inp[2] == 'o':
    #         if inp[3] == '!':
                1/0
