"""
# SITE: BitCoin.it/Wiki
# URL: https://en.bitcoin.it/wiki/Base58Check_encoding
# The Base58 symbol chart used in Bitcoin is specific to the Bitcoin project
# and is not intended to be the same as any other Base58 implementation used
# outside the context of Bitcoin (the characters excluded are: 0, O, I, and l).
# -----------------------------------------------
#
# code_string = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"
# x = convert_bytes_to_big_integer(hash_result)
## output_string = ""
#
# while(x > 0) {
#         (x, remainder) = divide(x, 58)
#         output_string.append(code_string[remainder])
#     }
#
# repeat(number_of_leading_zero_bytes_in_hash)  {
#     output_string.append(code_string[0]);
#     }
#
# output_string.reverse();
#\n\n"""
# print(__doc__)

import base64

def show_base64_len(string):
    string = string.encode()
    _a = base64.b64encode(string).decode()

    print("({1:>2}) {0:}".format(_a, len(_a)))


strings = [
    "outside the context of Bitcoin (the characters excluded are:",
    "9d55e1f7058e9a79725974caa41d1ba09d693c5d3e36506",
    "b29cbbbbc2ce5f0c7968b8be35b67a6c51b55",
    "ff73868b0024599a539a27f790691",
    "0000000000f1ef42420",
    "hello~ world!",

    "0",
    "1",
    "2",

    "a",
    "A",

    "b",
    "B",
    ]

for string in strings:
    show_base64_len(string)
