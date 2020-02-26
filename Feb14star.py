#!/usr/bin/env python
# -*- coding: utf8 -*-

height = 10

#for n in range(height):
#   print(" " * n, "*" * (height-n))

for n in range(height):
    print(" " * n + "*" * (height-n))

for n in range(height-1, -1, -1):
    print(" " * n + "*" * (2*(height-n-1)+1))

for n in range(height-2, 0, -1):
    print(" " * n + "* " * (height-n))
