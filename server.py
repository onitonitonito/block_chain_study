# import json
# from textwrap import dedent

from flask import Flask, jsonify, request, render_template, redirect
from uuid import uuid4

from block_class.block_chain import BlockChain

app = Flask(__name__)

# 32-bits 유니크 아이디를 생성한다 - '11864aaa-d1b2-45af-9c5a-c21dda71c6fc'
node_identifier = str(uuid4()).replace("-", "")

bc = BlockChain()

@app.route('/', methods=['GET'])
def index():
    return "HELLO!"


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


@app.route('/transactions/new', methods=['GET','POST'])
def new_transaction():

    if request.method == 'POST':
        # values = request.get_json()

        sender = request.form['sender']
        recipient = request.form['recipient']
        amount = request.form['amount']

        values = {
            'sender': sender,
            'recipient': recipient,
            'amount': amount }

        required = ['sender', 'recipient', 'amount']

        if not all(k in values for k in required):
            return "... missing values ...", 400

        index = bc.new_transaction(
            values['sender'],
            values['recipient'],
            values['amount'])

        response = {
            'message': '... Transaction will be added to Block {0}'.format(index)
        }
        return jsonify(response), 201

    else:
        return render_template("./new_TX.html"), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
