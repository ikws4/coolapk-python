from api import api
from utils import image
from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime


# 暂存储用户数据
STORE = {}


def upload_avatar_job():
    img = image.generate_time_image()
    now = datetime.now()
    user = STORE.get('user')
    print(f"upload avatar({now}): {api.upload_avatar(user, img)}")


def main():
    u = input('username: ')
    p = input('password: ')
    user = api.login(u, p)
    STORE['user'] = user

    print('starting execute job...')

    scheduler = BlockingScheduler()
    now = datetime.now()
    scheduler.add_job(
        upload_avatar_job,
        'interval',
        minutes=1,
        start_date=now.replace(second=0, microsecond=0),
    )
    scheduler.start()


if __name__ == '__main__':
    main()
