#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

# decorate from 42
def decorate(function):
    """ Function decorator demo."""
    print('Now executing function Decorate, decorating', function.__name__)
    def wrap_function(*args):
        print('Now executing', function.__name__)
        return function(*args)
    return wrap_function

# reminders on functions

# assign functions to variables
def greet(name):
    return 'Hello ' + name

if __name__ == '__main__':
    print()

# decorate from 42
    decorate(print)
    decorate(len)
# assign functions to variables
    greet_someone = greet
    print(greet_someone('John'))

    print()
