import os
import json
from pprint import pprint

DIRS = os.path.dirname(__file__).partition("block_chain_study\\")
ROOT = DIRS[0] + DIRS[1]
FILE_W_DIR = ROOT + "/block_class/block.json"

with open(FILE_W_DIR) as f:
    data = json.load(f)


pprint(data)
print("\n\n", type(data))

print("\
    \n(1) Sender   = {0} \
    \n(2) Recipent = {1} \
    \n(3) Amount   = {2}".format(
        data['transaction'][0]['sender'],
        data['transaction'][0]['recipient'],
        data['transaction'][0]['amount'],)
    )
