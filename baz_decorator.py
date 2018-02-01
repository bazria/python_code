#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

def decorate(function):
    """ Function decorator demo."""
    print('Now executing function Decorate, decorating', function.__name__)
    def wrap_function(*args):
        print('Now executing', function.__name__)
        return function(*args)
    return wrap_function

if __name__ == '__main__':
    # execute only if run as a script
    print()
    print('''OK, Dude...''')
    print()
    decorate(print)
