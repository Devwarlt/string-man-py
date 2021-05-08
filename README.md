# string-man-py [![license-badge]][license]
String manipulation using Python with Flask framework.

## Languages
![py-language-badge]

## Tests

### cURL -> GET ROT-13 Encrypt

```shell
curl --request GET http://127.0.0.1:3200/rot13/encrypt?plain_text=Hello,%20world! | python -m json.tool
```

### cURL -> GET ROT-13 Decrypt

```shell
curl --request GET http://127.0.0.1:3200/rot13/decrypt?rot13_encrypted_text=Uryyb,%20jbeyq! | python -m json.tool
```

### cURL -> POST ROT-13 Encrypt

```shell
curl --header "Content-Type: application/json" --request POST --data '{"\"plain_text"\":"\"Hello, world!"\"}' http://127.0.0.1:3200/rot13/encrypt | python -m json.tool
```

### cURL -> POST ROT-13 Decrypt

```shell
curl --header "Content-Type: application/json" --request POST --data '{"\"rot13_encrypted_text"\":"\"Uryyb, jbeyq!"\"}' http://127.0.0.1:3200/rot13/decrypt | python -m json.tool` | **POST** | `/rot13/decrypt
```

---

### Contributors
- Nádio ~ [@Devwarlt][nadio-ref]
- João Evangelista

[nadio-ref]: https://github.com/Devwarlt

[py-language-badge]: https://img.shields.io/badge/Python-3.8-black?logo=python&style=plastic

[license-badge]: https://img.shields.io/badge/License-MIT-black?style=plastic
[license]: /LICENSE
