from werkzeug.datastructures import ImmutableMultiDict
from flask.wrappers import Request
from flask import jsonify
from repositories import rot13_repository
from traceback import format_exc
from json import loads
import logging


def encrypt(request: Request) -> str:
    result: dict = {}
    try:
        if request.method == 'GET':
            body: ImmutableMultiDict = request.args
            plain_text: str = body.get('plain_text', type=str)
            if not plain_text:
                result.update({
                    'status': 400,
                    'response': "Missing argument 'plain_text' on request"
                })
            else:
                rot13_encrypted_text: str = rot13_repository\
                    .Rot13.encrypt(plain_text)
                result.update({
                    'status': 200,
                    'response': {
                        'plain_text': plain_text,
                        'rot13_encrypted_text': rot13_encrypted_text
                    }
                })

        if request.method == 'POST':
            decoded_data: str = request.data.decode('utf-8')
            if decoded_data.startswith("\'")\
                    and decoded_data.endswith("\'"):
                decoded_data = decoded_data[1:-1]

            body: dict = loads(decoded_data)
            plain_text: str = body.get('plain_text')
            if not plain_text:
                result.update({
                    'status': 400,
                    'response': "Missing argument 'plain_text' on request"
                })
            else:
                rot13_encrypted_text: str = rot13_repository\
                    .Rot13.encrypt(plain_text)
                result.update({
                    'status': 200,
                    'response': {
                        'plain_text': plain_text,
                        'rot13_encrypted_text': rot13_encrypted_text
                    }
                })
    except Exception:
        stacktrace: str = format_exc()
        logging.getLogger(__name__).error(stacktrace)
        result.update({
            'status': 500,
            'response': "Internal Server Error",
            'stacktrace': stacktrace
        })
    result.update({'method': request.method})
    return jsonify(result)


def decrypt(request: Request) -> str:
    result: dict = {}
    try:
        if request.method == 'GET':
            body: ImmutableMultiDict = request.args
            rot13_encrypted_text: str = body.get(
                'rot13_encrypted_text', type=str)
            if not rot13_encrypted_text:
                result.update({
                    'status': 400,
                    'response': "Missing argument 'rot13_encrypted_text' on request"
                })
            else:
                plain_text: str = rot13_repository\
                    .Rot13.decrypt(rot13_encrypted_text)
                result.update({
                    'status': 200,
                    'response': {
                        'plain_text': plain_text,
                        'rot13_encrypted_text': rot13_encrypted_text
                    }
                })

        if request.method == 'POST':
            decoded_data: str = request.data.decode('utf-8')
            if decoded_data.startswith("\'")\
                    and decoded_data.endswith("\'"):
                decoded_data = decoded_data[1:-1]

            body: dict = loads(decoded_data)
            rot13_encrypted_text: str = body.get('rot13_encrypted_text')
            if not rot13_encrypted_text:
                result.update({
                    'status': 400,
                    'response': "Missing argument 'rot13_encrypted_text' on request"
                })
            else:
                plain_text: str = rot13_repository\
                    .Rot13.decrypt(rot13_encrypted_text)
                result.update({
                    'status': 200,
                    'response': {
                        'plain_text': plain_text,
                        'rot13_encrypted_text': rot13_encrypted_text
                    }
                })
    except Exception:
        stacktrace: str = format_exc()
        logging.getLogger(__name__).error(stacktrace)
        result.update({
            'status': 500,
            'response': "Internal Server Error",
            'stacktrace': stacktrace,
            'method': request.method
        })
    result.update({'method': request.method})
    return jsonify(result)
