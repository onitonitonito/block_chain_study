"""
# Digital Signiture (ECDSA) - Practice
# pyBitCoinTools (https://pypi.python.org/pypi/bitcoin)
#        written by - Vitalik Buterin
#        file = 2-11_ECDSA_01.py
#\n\n"""
print(__doc__)

import bitcoin.main as btc


d = btc.random_key()
Q = btc.privkey_to_pubkey(d)
