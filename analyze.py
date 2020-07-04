#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

plik = 'file'

def read():
    with open(plik, 'r') as read:
        lines = read.readlines()
        for line in lines:
            str = line.split()
            analyzeline(str)

def analyzeline(line):