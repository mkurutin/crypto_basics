#!/usr/bin/env python
from utils import *

def read_known_key():
    return read_hex_file('key.txt')

def get_known_plain_text(cipher_file):
    return ''.join(to_char(xor(read_known_key(),
        read_hex_file(cipher_file))))

def show_plain_text_promt(cipher_file):
    known_plain_text = get_known_plain_text(cipher_file)
    plain_text = raw_input("Known plain text for the cipher is: {0}". \
            format(known_plain_text))
    known_plain_text+=plain_text
    return known_plain_text

def rewrite_key(key_int_arr):
    f = open("key.txt", "w")
    f.write(to_hex_string(key_int_arr) + '\n')
    f.close

def main():
    file_name = raw_input("Please enter name of a file that holds a cipher: ")
    plain_text = show_plain_text_promt(file_name)
    key = xor(read_hex_file(file_name), plain_to_int_arr(plain_text))
    rewrite_key(key)
    print 'Newly generated key:'
    print key

main()
