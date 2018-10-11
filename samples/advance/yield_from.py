# -*- coding: utf-8 -*-
def gen1():
    for c in 'AB':
        yield c

def gen2():
    yield from 'AB'

print(list(gen1()))
print(list(gen2()))