#!/usr/bin/env python

d = {}
d.setdefault('a', {}).setdefault('b', []).append(1)
print(d)