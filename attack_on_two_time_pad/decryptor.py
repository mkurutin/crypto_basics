#! /usr/bin/env python
from utils import *

def strxor(int_arr1, int_arr2):
    return to_char(xor(int_arr1, int_arr2))

def xor_files(file_name1, file_name2):
    return strxor(read_hex_file(file_name1), \
        read_hex_file(file_name2))

def collect():
    collection = []
    for x in range(1, 11):
        collection.append(xor_files("cipher%d.txt" % x, "cipher11.txt"))
    return zip(*collection)

def main():
    for x in collect():
        print x

main()
