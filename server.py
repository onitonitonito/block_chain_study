# import json
# from textwrap import dedent

from flask import Flask, jsonify, request, render_template, redirect
from uuid import uuid4

from block_class.block_chain import BlockChain

app = Flask(__name__)

# 32-bits 유니크 아이디를 생성한다 - '11864aaa-d1b2-45af-9c5a-c21dda71c6fc'
node_identifier = str(uuid4()).replace("-", "")

bc = BlockChain()

@app.route("/", methods=["GET"])
def index():
    return render_template('./chain_help.html')


@app.route("/chain", methods=["GET"])
def full_chain():
    response = {
        "chain": bc.chain,
        "length": len(bc.chain),
    }

    return jsonify(response), 200


@app.route("/mine", methods=["GET"])
def mine():
    last_block = bc.last_block
    last_proof = last_block["proof"]

    proof = bc.proof_of_work(last_proof)

    bc.new_transaction(
        sender="0",
        recipient = node_identifier,
        amount= 1)

    previous_hash = bc.hash(last_block)
    block = bc.new_block(proof, previous_hash)

    response = {
        "message" :         "... new block forged",
        "index" :           block["index"],
        "transactions" :    block["transactions"],
        "proof" :           block["proof"],
        "previous_hash" :   block["previous_hash"]
    }

    return jsonify(response), 200


@app.route("/transactions/new", methods=["GET","POST"])
def new_transaction():

    if request.method == "POST":
        # values = request.get_json()

        sender = request.form["sender"]
        recipient = request.form["recipient"]
        amount = request.form["amount"]

        values = {
            "sender": sender,
            "recipient": recipient,
            "amount": amount }

        required = ["sender", "recipient", "amount"]

        if not all(k in values for k in required):
            return "... missing values ...", 400

        index = bc.new_transaction(
            values["sender"],
            values["recipient"],
            values["amount"])

        response = {
            "message": "... Transaction will be added to Block {0}".format(index),
            "current TX" : bc.current_transactions
        }
        return jsonify(response), 201

    else:
        return render_template("./new_TX.html"), 200


@app.route("/transactions", methods=["GET"])
def show_transaction():
    response = bc.current_transactions
    return jsonify(response), 200


@app.route("/write", methods=["GET"])
def write_chains():
    response = {
        "message": "...  Writing whole chains to chains.json ..."
    }
    return jsonify(response), 200



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
