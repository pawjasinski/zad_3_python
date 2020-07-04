#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import sys
import os

if __name__ == "__main__":

    if len(sys.argv) > 2:
        input("Niepoprawny arg, exit, press any key")
        sys.exit(1)

    for plik in sys.argv:
        if plik == sys.argv[0]:
            continue
        print(plik)

    for file in sys.argv:
        if plik == sys.argv[0]:
            continue
        try:
            with open(file, 'r') as r, open(file+'b.txt', 'r') as w:
                lines = r.readlines()

                for line in lines:
                    if not line.isspace():
                    w.write(line.replace(' ', ''))
        except IOError:
            input('could not open file ' + file + ' press any key')
            sys.exit(1)
