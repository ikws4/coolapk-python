import time
import hashlib
import base64


DEVICE_ID = "8513efac-09ea-3709-b214-95b366f1a185"


def get_app_token() -> str:
    now = int(time.time())
    hex_now = hex(now)
    md5_now = hashlib.md5(str(now).encode('utf-8')).hexdigest()
    s = f'token://com.coolapk.market/c67ef5943784d09750dcfbb31020f0ab?{md5_now}${DEVICE_ID}&com.coolapk.market'
    md5_s = hashlib.md5(base64.b64encode(s.encode('utf-8'))).hexdigest()
    token = md5_s + DEVICE_ID + hex_now
    return token


def get_request_hash(text: str) -> str:
    start = text.index('requestHash : ') + 15
    end = start + 14
    return text[start:end]
