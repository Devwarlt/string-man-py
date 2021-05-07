from flask import Flask
from flask_cors import CORS

app: Flask = Flask(__name__)

CORS(
    app,
    origins='*',
    allow_headers=[
        'Origin',
        'X-Requested-With',
        'Content-Type',
        'Accept',
        'x-access-token'
    ],
    methods=[
        'GET',
        'POST',
        'PUT',
        'DELETE',
        'OPTIONS'
    ]
)
