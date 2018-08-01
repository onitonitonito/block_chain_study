"""
* 블럭정보.json 를 읽어서, 거래 정보를 추출한다.
* 마이닝시 보상이 발생하므로, 매 블럭 거래정보 있음
"""

import os
import json
from pprint import pprint

FILE = "/block_class/chains_old.json"

DIRS = os.path.dirname(__file__).partition("block_chain_study\\")
FILE_W_DIR = DIRS[0] + DIRS[1] + FILE


def get_json(file_w_dir):
    with open(file_w_dir, mode='r') as f:
        chains = json.load(f)
    return chains


def show_transaction(chains):
    for n in range(len(chains)):

        # 블럭 마이닝 보상거래 1개 이상의 거래가 존재 할 경우
        if len(chains[n]['transactions']) > 1:
            print("\n\n------ index.%s / [%s] -------" %(
                chains[n]['index'],
                len(chains[n]['transactions'])-1),
                end="")

            for m in range(len(chains[n]['transactions'])):

                # 마이닝 보상거래는 출력에서 제외 (보상: sender="0")
                if chains[n]['transactions'][m]['sender'] is "0":
                    pass

                else:
                    print("\
                        \n* Sender   = {0} \
                        \n* Recipent = {1} \
                        \n* Amount   = {2:,}".format(
                        chains[n]['transactions'][m]['sender'],
                        chains[n]['transactions'][m]['recipient'],
                        int(chains[n]['transactions'][m]['amount']),)
                    )
        else:
            print("\n\n... index : %s ... NO TRANSACTIONS IN THIS LEDGER!\
                    \n      (ONLY MINNING CONPENSATION or NOT)..." % (n + 1))



if __name__ == '__main__':
    # json 에서 전체 체인정보를 읽어온다.
    chains = get_json(FILE_W_DIR)

    # 전체 json 정보를 출력해서 확인한다
    # pprint(chains)

    # 체인에서 거래정보만 추출해서 보여준다 (블럭보상은 제외 함)
    show_transaction(chains)
