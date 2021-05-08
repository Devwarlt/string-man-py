from flask import request
from flask.json import jsonify
from flask_cors import cross_origin
from controllers import (
    text_controller,
    rot13_controller
)
from core import app


@cross_origin()
@app.route('/outshine', methods=['POST'])
def outshine_handler() -> str:
    return text_controller.text_out(request)


@cross_origin()
@app.route('/rot13/encrypt', methods=['GET', 'POST'])
def rot13_encrypt_handler() -> str:
    return rot13_controller.encrypt(request)


@cross_origin()
@app.route('/rot13/decrypt', methods=['GET', 'POST'])
def rot13_decrypt_handler() -> str:
    return rot13_controller.decrypt(request)


@cross_origin()
@app.route('/test', methods=['GET', 'POST'])
def test_handler() -> str:
    return jsonify({
        'status': 200,
        'response': f"Hello, world!"
    })
