#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import sys
import os
import fileinput
os.chdir(os.getcwd())

if __name__ == "__main__":
    #os.chdir(os.getcwd())
    #print(os.getcwd())

    if len(sys.argv) != 2:
        input("Niepoprawny argument, exit, press key")
        exit(1)

    print(sys.argv[1])

    file_or = sys.argv[1]
    file_b = file_or + 'b.txt'

    with open(file_or,'r') as r, open(file_b, 'w') as w:
        lines = r.readlines()

        for line in lines:
            if not line.isspace():
                w.write(line.replace(" ", ""))