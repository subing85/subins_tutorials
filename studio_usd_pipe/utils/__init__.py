import getpass

from datetime import datetime


def get_datetime():
    return datetime.now().strftime('%Y/%d/%B - %I:%M:%S:%p')


def get_user():
    return getpass.getuser()
