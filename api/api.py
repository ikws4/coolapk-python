import requests
import random
from .helper import get_request_hash, get_app_token
from .models import User


def _base_post(url, **kwargs):
    """POST请求封装

    Args:
        url (str): url.
        **kwargs:  **kwargs for `request.post`.

    Returns:
        requests.Response: 请求返回体.

    """
    url = 'https://api.coolapk.com' + url
    headers = {
        'X-Requested-With': 'XMLHttpRequest',
        'X-App-Id': 'com.coolapk.market',
        'X-App-Token': get_app_token()
    }
    res = requests.post(url, headers=headers, **kwargs)
    return res


def login(u, p):
    """模拟酷安登录
    通过 cookies 获取 token username uid 转为 `User` 对象

    Args:
        u (str): 用户名、手机号、邮箱
        p (str): 密码

    Returns:
        User

    """
    url = 'https://account.coolapk.com/auth/loginByCoolAPk'
    res = requests.get(url)

    # TODO: 验证码识别

    data = {
        'submit': 1,
        'requestHash': get_request_hash(res.text),
        'login': u,
        'password': p,
        'captcha': ''
    }
    headers = {
        'x-requested-with': 'XMLHttpRequest'
    }
    res = requests.post(url, data, headers=headers, cookies=res.cookies)

    return User(**res.cookies.get_dict())


def upload_avatar(uses, image):
    """上传头像

    Args:
        user (User): 用户对象
        image: 图片路径 或 字节数据

    Returns:
        bool: 上传成功返回 True

    """
    if isinstance(image, str):
        image = open(image, 'rb')

    files = {
        'imgFile': (str(random.random()), image, 'image/jpeg')
    }
    res = _base_post('/v6/account/changeAvatar',
                     cookies=user.__dict__, files=files)

    if res.json().get('message'):
        return False
    else:
        return True
