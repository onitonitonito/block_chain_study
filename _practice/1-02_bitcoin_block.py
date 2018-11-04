"""
# blockChain API Documentation
# https://www.blockchain.com/api/blockchain_api
#
# Single Block
# --------------------------------------------
# https://blockchain.info/rawblock/$block_hash
# You can also request the block to return in binary form
# (Hex encoded) using ?format=hex
#\n\n"""
print(__doc__)

import time
import requests
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pprint import pprint

print("read today's blocks")

url = "https://blockchain.info/blocks?format=json"
res = requests.get(url=url)
data = res.json()

blocks = data['blocks']

header = []
header_brief = []

for n in range(len(blocks)):
    height = blocks[n]['height']
    b_time = blocks[n]['time']
    b_hash = blocks[n]['hash']

    header.append([height, b_time, b_hash])
    header_brief.append([height, b_time, b_hash[:35]+'....'])


# read yesterday's blocks
stime = b_time - 24 * 60 * 60


# read blocks generated during last 10 days
for n_day in range(0, 10):
    pass

print("\n[_Height_],[__Time__], [________Block-Hash 35-heading__________],")
pprint(header_brief)







"""
# json file format
pprint(blocks)
[
    {'hash': '000000000000000000054058cb421254c58d7c12c4e18970a07ef41d0cbc170e',
     'height': 550928,
     'main_chain': True,
     'time': 1542785999},

    {'hash': '0000000000000000001647f96c634d9230f97c92779e5a502cabe07acd65b8c1',
     'height': 550927,
     'main_chain': True,
     'time': 1542782621},
]
"""
