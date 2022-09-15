#!/usr/bin/env python3
from dev_aberto import hello
from babel.numbers import format_number
from datetime import datetime
import locale
import gettext

if __name__ == '__main__':
    gettext.install('cli', localedir='locale') 
    # date, name = '2022-09-12T20:10:47Z', "Rafael"
    date, name = hello()
    print(_('Last commit made in:'), datetime.strftime(datetime.strptime(date, '%Y-%m-%dT%H:%M:%SZ'), "%d/%m/%Y %H:%M:%S"), _(' by'), name)