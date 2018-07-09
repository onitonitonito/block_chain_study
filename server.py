from flask import Flask, jsonify, request
import json
from textwrap import dedent
from uuid import uuid4

from block_class.block_chain import BlockChain

app = Flask(__name__)
node_identifier = str(uuid4()).replace("-", "")

bc = BlockChain()

@app.route('/mine', methods=['GET'])
def mine():
    return "... We'll mine a new Block ..."

@app.route('/transactions/new', methods=['POST'])
def new_transaction():
    request.on_json_loading_failed = on_json_loading_failed_return_dict

    values = request.get_json()
    required = ['sender', 'recipient', 'amount']

    if not all(k in values for k in required):
        return "... missing values ...", 400

    index = bc.new_transaction(values['sender'], values['recipient'], values['amount'])

    response = {
        'message': '... Transaction will be added to Block {0}'.format(index)
    }

    return jsonify(response), 201


@app.route('/chain', methods=['GET'])
def full_chain():
    response = {
        'chain': bc.chain,
        'length': len(bc.chain),
    }

    return jsonify(response), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
