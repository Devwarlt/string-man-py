from flask.wrappers import Request
from flask import jsonify
from repositories import text_repository
from traceback import format_exc
from json import loads
import logging


def text_out(request: Request) -> str:
    result: dict = {}
    try:
        decoded_data: str = request.data.decode('utf-8')
        if decoded_data.startswith("\'")\
                and decoded_data.endswith("\'"):
            decoded_data = decoded_data[1:-1]

        body: dict = loads(decoded_data)
        enter_text: str = body.get('text')
        enter_words: list = body.get('wordlist')
        send_text: str = text_repository.text_out(enter_text, enter_words)
        result.update({
            'status': 200,
            'response': send_text
        })
    except Exception:
        stacktrace: str = format_exc()
        logging.getLogger(__name__).error(stacktrace)
        result.update({
            'status': 500,
            'response': "Internal Server Error",
            'stacktrace': stacktrace
        })
    return jsonify(result)
