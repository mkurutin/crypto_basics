import re
import os.path

def plain_to_int_arr(string):
    return map(lambda x: ord(x), string)

def read_hex_file(file_name):
    try:
        with open(file_name, 'r') as f:
            content = f.read()
            return to_int_array(content.rstrip())
    except IOError:
        return []

def to_int_array(hex_string):
    return map(lambda x: int(x, 16), re.findall('..', hex_string))

def xor(int_arr1, int_arr2):
    return [x^y for (x,y) in zip(int_arr1, int_arr2)]

def to_char(int_arr):
    return map(lambda x: chr(x), int_arr)

def to_hex_string(int_arr):
    return ''.join(map(lambda x: "{:02x}".format(x), int_arr))
