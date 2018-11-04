"""
# Digital Signiture (ECDSA) - Practice
# pyBitCoinTools (https://pypi.python.org/pypi/bitcoin)
#        written by - Vitalik Buterin
#        file = 2-11_ECDSA_02.py
#\n\n"""
print(__doc__)

import bitcoin.main as btc


d = btc.random_key()
Q = btc.privkey_to_pubkey(d)


"""
print(len(d),"= ", d)
print(len(Q),"= ", Q)
"""
# len = 64 Hex (32 bytes)  ... hash random_key
# len = 130 Hex (65 bytes) = 32 bytes(64) + 32 bytes(64) + 1 byte (2)
# hash of co-ordinates(x,y) on ECCA and add classification 1 byte

x = "Hello Alice?"
x = x.encode()

sig = btc.ecdsa_sign(x, d)
verify = btc.ecdsa_verify(x, sig, Q)

print("Message = '{}'".format(x.decode()))

if verify:
    print("\n Valid Signiture")
else:
    print("\n *** Invalid Signiture ***")
