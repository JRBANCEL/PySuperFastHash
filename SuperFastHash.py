#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Python implementation of SuperFastHash algorithm
"""

import binascii
import sys

def get16bits(data):
    return int(binascii.hexlify(data[1::-1]), 16)

def superFastHash(data):
    hash = length = len(data)
    if length == 0:
        return 0

    rem = length & 3
    length >>= 2

    while length > 0:
        hash += get16bits(data) & 0xFFFFFFFF
        tmp = (get16bits(data[2:])<< 11) ^ hash
        hash = ((hash << 16) & 0xFFFFFFFF) ^ tmp
        data = data[4:]
        hash += hash >> 11
        length -= 1

    if rem == 3:
        hash += get16bits (data)
        hash ^= (hash << 16) & 0xFFFFFFFF
        hash ^= (int(binascii.hexlify(data[2]), 16) << 18) & 0xFFFFFFFF
        hash += hash >> 11
    elif rem == 2:
        hash += get16bits (data)
        hash ^= (hash << 11) & 0xFFFFFFFF
        hash += hash >> 17
    elif rem == 1:
        hash += int(binascii.hexlify(data[0]), 16)
        hash ^= (hash << 10) & 0xFFFFFFFF
        hash += hash >> 1

    hash = hash & 0xFFFFFFFF
    hash ^= (hash << 3) & 0xFFFFFFFF
    hash += hash >> 5
    hash ^= (hash << 4) & 0xFFFFFFFF
    hash += hash >> 17
    hash ^= (hash << 25) & 0xFFFFFFFF
    hash += hash >> 6

    return hash

if __name__ == "__main__":
    print hex(superFastHash(sys.argv[1]))
