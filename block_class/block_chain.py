"""
* 블록체인 구현 (블록생성, 트랜잭션, 작업증명, 마이닝)
* https://goo.gl/M6XU5v
"""
import hashlib
import json
from time import time
from uuid import uuid4


class BlockChain(object):
    def __init__(self):
        self.chain = []
        self.current_transactions = []

        self.new_block(proof=100, previous_hash=1)          # genesis block

    def new_block(self, proof, previous_hash=None):
        # Creates a new Block and adds it to the chain
        block = {
            "index": len(self.chain) + 1,
            "timestamp": time(),
            "transactions": self.current_transactions,
            "proof": proof,
            "previous_hash": previous_hash or self.hash(self.chain[-1])
        }

        self.current_transactions = []
        self.chain.append(block)

        return block

    def new_transaction(self, sender, recipient, amount, hash=0):
        """ Creates a new transaction to go into the next mined Block
        : param sender: <str> Sender의 주소
        : param recipient: <str> Recipient의 주소
        : param amount: <int> Amount
        : return: <int> 이 거래를 포함할 블록의 index 값
        """

        if hash:
            sender = self.hash(sender)
            recipient = self.hash(recipient)

        self.current_transactions.append({
            'sender': sender,
            'recipient': recipient,
            'amount': amount,
        })

        return self.last_block['index'] + 1

    @staticmethod
    def hash(block):
        # Hashes a Block ... malfuntion with sort_keys=True option
        # block_string = json.dumps(block, sort_keys=True).encode()
        block_string = json.dumps(block).encode()
        return hashlib.sha256(block_string).hexdigest()

    @property
    def last_block(self):
        # Returns the last Block in the chain
        return self.chain[-1]

    def proof_of_work(self, last_proof):
        proof = 0
        while self.valid_proof(last_proof, proof) is False:
            proof += 1
        return proof

    @staticmethod
    def valid_proof(last_proof, proof):
        guess = str(last_proof * proof).encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash[:4] == "0000"


if __name__ == '__main__':
    from pprint import pprint

    # 오브젝트 선언하는 순간, 최최의 Genesis Block을 생성한다
    bc = BlockChain()

    pprint(bc.chain[-1])
    input("\n... 제네시스 블럭생성 ...\n\n\n")


    # 제네시스 블록을 해쉬해서 다음블록에 기록한다.
    blocks_hashed = bc.hash(bc.chain[-1])
    print ("\n... 젠블록에 해쉬함수 적용 / 길이 = {1} bits\
            \n{0} \n\n\n".format(blocks_hashed,len(blocks_hashed)))


    # 블록과 블록사이에서, 2개의 트랜젝션이 발생한다.
    bc.new_transaction(sender='Scrouge', recipient='Alice', amount=200, hash=0)
    bc.new_transaction(sender='Alice', recipient='Bob', amount=150, hash=0)
    pprint(bc.current_transactions)
    input("\n... 트랜잭션 2개 발생 ...\n\n\n")


    # 새로운 블럭이 발생하면, 이전블록 해쉬와 거래정보가 자동으로 기록된다.
    bc.new_block(proof=100)
    pprint(bc.chain)
    input("\n... 새로운 블럭생성(마이닝)...\
        \n... 자동으로 트랜젝션과 이전해쉬가 기록 (가독성을 위해 해쉬변환 생략) ...\
        \n\n\n")


    # 이전 블록정보를 해쉬한다 (마지막 블럭정보)
    blocks_hashed = bc.hash(bc.chain[-1])
    print ("\n... 이전블록에 해쉬함수 적용 / 길이 = {1} bits\
    \n{0} \n\n\n".format(blocks_hashed,len(blocks_hashed)))


    # 블록과 블록사이에서, 새로운 1개의 트랜젝션이 발생한다.
    bc.new_transaction(sender='Scrouge', recipient='Charlie', amount=1000, hash=0)
    pprint(bc.current_transactions)
    input("\n... 트랜잭션 1개 발생 ...\n\n\n")


    # 새로운 블록이 생성되면, 그동안 발생한 거래와 이전블럭 해쉬를 자동으로 기록한다.
    bc.new_block(proof=100)
    pprint(bc.chain)
    input("\n... 새로운 블럭생성(마이닝)...\
        \n... 자동으로 트랜젝션과 이전해쉬가 기록 (가독성을 위해 해쉬변환 생략) ...\
        \n\n\n")
