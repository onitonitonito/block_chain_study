import json
from pprint import pprint

FILE_W_DIR="C:/Users/nitt0/Documents/Github/block_chain_study/block_class/block.json"

with open(FILE_W_DIR) as f:
    data = json.load(f)


pprint(data)
print("\n\n", type(data))

print("(1) Sender   = %s" % data['transaction'][0]['sender'])
print("(2) Recipent = %s" % data['transaction'][0]['recipient'])
print("(3) Amount   = %s" % data['transaction'][0]['amount'])
