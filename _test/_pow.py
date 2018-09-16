"""
# 해쉬값의 마지막 자리가 '0'일 때까지 proof값을 1씩 증가 시키며 찾는다.
# 우연히 첫자리가 '0000'으로 시작하는 해쉬를 발견 했을 때,
# 작업 증명을 완성 한다. 작업증명(Proof of Work) 값은 proof=7725 이다.
"""
# print(__doc__)

import time

from pprint import pprint
from hashlib import sha256

MINING_UID = 'node_identifier_uid'

TRANSACTIONS = [
        {
            'sender': 'Alice',
            'recipient': 'Bob',
            'amount': 1000
        },
        {
            'sender': 'Scrouge',
            'recipient': 'Alice',
            'amount': 800
        },
        {
            'sender': 'coinbase_reward',
            'recipient': MINING_UID,
            'amount': 200
        },
    ]


block = {
        'index': 12,
        'difficulty': '0000000',
        'nonce': 0,
        'hash_previous': '0000000a8482b821aff9b2ce6103f69e',
        'transaction': TRANSACTIONS,
    }


def get_hash_w_nonce(block, nonce):
    """ 최근 블럭에 Nonce를 대입하여 해쉬값을 리턴한다"""
    block['nonce'] = nonce
    hash = sha256(str(block).encode()).hexdigest()
    return hash


def add_header(block, block_hash):
    """ Block Header에 Time-stamp와 계산 된 블럭해쉬를 기록"""
    header = {
        'timestamp': time.time(),
        'hash_present': block_hash, }
    for _key, _val in header.items():
        block[_key] = _val
    return block


def proof_of_work(block):
    nonce = 0
    difficulty = block['difficulty']

    while True:
        hash = get_hash_w_nonce(block, nonce)

        if hash[:len(difficulty)] == difficulty:
            hash_present = hash[:32]
            add_header(block, hash_present)
            return block
        nonce += 1


if __name__ == '__main__':
    block = proof_of_work(block)
    pprint(block)
