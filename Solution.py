#!/bin/python

_, m = input(), 10 ** 9 + 7
print reduce(lambda a, b : a * b % m, [1 + pow(2, int(x), m) for x in raw_input().split()], 1) - 1
