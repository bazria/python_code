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
def greet_01(name):
    return 'Hello ' + name

# define functions inside other functions
def greet_02(name):
    def get_message():
        return 'Hello '
    result = get_message() + name
    return result

# functions can be passed as parameters to other functions
def call_function(function):
    other_name = 'Ringo'
    return function(other_name)

# functions can return other functions
def compose_greet_function():
    def get_message():
        return 'Hello George!'
    return get_message

# inner functions have access to the enclosing scope
def compose_greet_function_02(name):
    def get_message():
        return 'Hello there ' + name + '!'
    return get_message



# decorators

# composition of decorators
def get_text(name):
    return 'lorem ipsum, {0} dolor sit amet'.format(name)

def p_decorate(function):
    def function_wrapper(name):
        return '<p>{0}</p>'.format(function(name))
    return function_wrapper



if __name__ == '__main__':
    print()

# decorate from 42
    decorate(print)
    decorate(len)
# assign functions to variables
    greet_someone = greet_01
    print(greet_someone('John'))
# define functions inside other functions
    print(greet_02('Paul'))
# functions can be passed as parameters to other functions
    print(call_function(greet_01))
# functions can return other functions
    greet = compose_greet_function()
    print(greet())
# inner functions have access to the enclosing scope
    greet = compose_greet_function_02('Mick')
    print(greet())
# composition of decorators
    my_get_text = p_decorate(get_text)
    print(my_get_text('Keith'))
    get_text = p_decorate(get_text)
    print(get_text('Brian'))

    print()
