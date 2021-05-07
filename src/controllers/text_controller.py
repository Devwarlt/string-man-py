from flask.wrappers import Request
from repositories import text_repository
from traceback import format_exc
from json import loads
import logging


def text_out(req: Request) -> tuple:
    try:
        body: dict = loads(req.data.decode('utf-8'))
        enter_text: str = body.get('text')
        enter_words: list = body.get('wordlist')
        send_text: str = text_repository.text_out(enter_text, enter_words)
        return send_text, 200
    except Exception:
        logging.getLogger(__name__).error(format_exc())
        return "Internal Server Error", 500
