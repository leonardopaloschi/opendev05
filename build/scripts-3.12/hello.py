#!python
from dev_aberto import hello
import gettext
from babel.dates import format_datetime
from datetime import datetime
import os

gettext.bindtextdomain('cli', 'locale')
gettext.textdomain('cli')
_ = gettext.gettext




if __name__ == '__main__':
    date, name = hello()
    locale = os.getenv('LANG', 'en_US.UTF-8').split('.')[0]
    date_obj = datetime.strptime(date, '%Y-%m-%dT%H:%M:%SZ')
    date = format_datetime(date_obj, locale=locale)

    str1 = (_('Last commit made on: '))
    str2 = (_(' by '))

    print(str1 + date + str2 + name)