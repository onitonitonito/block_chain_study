import json

from flask import Flask, jsonify, request, render_template, redirect
from uuid import uuid4
from textwrap import dedent

from block_class.block_chain import BlockChain

app = Flask(__name__)
node_identifier = str(uuid4()).replace("-", "")

bc = BlockChain()

@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'GET':
        return render_template("./index.html"), 200

    else:
        sender = request.args.get['sender']
        recipient = request.args.get['recipient']
        amount = request.args.get['amount']

        return bc.new_transaction(
            sender=sender,
            recipient=recipient,
            amount=amount,
            hash=0
            )

@app.route('/chain', methods=['GET'])
def full_chain():
    response = {
        'chain': bc.chain,
        'length': len(bc.chain),
    }

    return jsonify(response), 200


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

    index = bc.new_transaction(
        values['sender'], values['recipient'], values['amount'])

    response = {
        'message': '... Transaction will be added to Block {0}'.format(index)
    }

    return jsonify(response), 201


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
