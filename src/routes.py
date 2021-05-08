from flask import request as req
from flask_cors import cross_origin
from controllers import text_controller
from core import app
import urllib


@cross_origin()
@app.route('/outshine', methods=['POST'])
def outshine_handler() -> tuple:
    result, status = text_controller.text_out(req)
    if status != 200:
        return "<h1>Internal Server Error</h1>", 500
    return result, 200


@cross_origin()
@app.route('/teste', methods=['GET', 'POST'])
def teste_handler() -> tuple:
    return "Hello, world!", 200
