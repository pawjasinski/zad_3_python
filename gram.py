#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

class gram:
    def __init__(self, length = 0):
        self.str = ''
        self.count = 0
        self.length = length
        self.words = set()

    def push(self, other):
        if len(other) != self.length:
            print('bad length argument')
            return
        self.words.add(other)
        self.count += 1

    def sort(self):
        sorted(self.words)

    def remove(self, element):
        try:
            self.words.remove(element)
        except KeyError:
            print('cant remove, element is not in set')
            return element


    # for sorting
    def __lt__(self, other):
        return self.count < other.count

    # for loop, iterator
    def __iter__(self):
        return iter(self.words)