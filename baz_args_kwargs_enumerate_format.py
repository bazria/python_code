#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

import sys

def print_everything(titlestring, *args):
    print(titlestring)
    for count, thing in enumerate(args):
        # use format method to substitute
        print( '{0}...... {1}'.format(count, thing))

def print_table_things(titlestring, **kwargs):
    print(titlestring)
    for key, value in kwargs.items():
        print( '{0} === {1}'.format(key, value))

def print_three_things(a, b, c):
    print( 'a = {0}, b = {1}, c = {2}'.format(a, b, c))

def demo_args_kwargs(required_argument, *args, **kwargs):
    # required_arg is a positional-only argument
    print(required_argument)

    # args is a tuple of positional arguments because the argument name has * prepended
    if args:
        print(args)

    # kwargs is a dictionary of keyword arguments because the argument name has ** prepended
    if kwargs:
        print(kwargs)

if __name__ == '__main__':
    print('Number of arguments:', len(sys.argv))
    print('Argument list:', sys.argv)
    print()
    print("format string")
    print()
    print("ordered arguments:")
    base_string = '{0} bites the {1}'
    print(base_string)
    new_string = base_string.format('Another one', 'dust')
    print(new_string)
    print()

    print("named arguments:")
    base_string = '{who} bites the {what}'
    print(base_string)
    new_string = base_string.format(what = 'another one', who ='Dust', )
    print(new_string)
    print()

    print("string arguments, also with %i for integers, %f for float:")
    base_string = '%s bites the %s'
    print(base_string)
    new_string = base_string%('A', 'B')
    print(new_string)
    print()

    print("*args arguments: allow to pass an arbitrary number of arguments")
    print_everything('test *args', 'apple', 'banana', 'pear', 'cabbage')
    print()

    print("**kwargs arguments: allow to handle named arguments not defined in advance")
    print_table_things('test **kwargs', apple = 'fruit', cabbage = 'vegetable')
    print()

    my_list = ['coffee', 'cigarettes', 'chocolate']
    print('my list ', end = '')
    print_three_things(*my_list)
    print('my tuple ', end = '')
    my_tuple = ('coffee', 'cigarettes', 'chocolate')
    print_three_things(*my_tuple)
    print('my dictionary ', end = '')
    my_dict = {0: 'coffee', 1: 'cigarettes', 3: 'chocolate'}
    print_three_things(*my_dict)
    print()

    demo_args_kwargs('argument obligatoire')
    demo_args_kwargs('argument obligatoire', 'argument facultatif 1', 'argument facultatif 2', 'argument facultatif 3',  )
    demo_args_kwargs('argument obligatoire', 'argument facultatif 1', 'argument facultatif 2', 'argument facultatif 3', keyword_1 = 'mot-cle 1', keyword_2 = 'mot-cle 2', keyword_3 = 'etc...' )
