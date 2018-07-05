"""


"""
import hashlib
import json
from time import time


class Blockchain(object):
    def __init__(self):
        self.chain = []
        self.current_transactions = []

    def new_block(self):
        # Creates a new Block and adds it to the chain
        pass

    def new_transaction(self, sender, recipient, amount):
        """ Creates a new transaction to go into the next mined Block
        :param sender: <str> Sender의 주소
        :param recipient: <str> Recipient의 주소
        :param amount: <int> Amount
        :return: <int> 이 거래를 포함할 블록의 index 값
        """

        self.current_transactions.append({
            'sender': sender,
            'recipient': recipient,
            'amount': amount,
        })

        return self.last_block['index'] + 1

    @staticmethod
    def hash(block):
        # Hashes a Block
        pass

    @property
    def last_block(self):
        # Returns the last Block in the chain
        pass


if __name__ == '__main__':
    pass
