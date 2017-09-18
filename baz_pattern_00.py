#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

def pattern_01():
    """
    Print 5 rows of 5 stars.
    """
    print(pattern_01.__name__)
    print(pattern_01.__doc__.lstrip().rstrip())
    for row in range(5):
        for column in range(5):
            print('*', end = '')
        print()
    print()

def pattern_02():
    """
    Print 12345 on 5 rows.
    """
    print(pattern_02.__name__)
    print(pattern_02.__doc__.lstrip().rstrip())
    for row in range(5):
        for column in range(1, 6):
            print(column, end = '')
        print()
    print()

def pattern_02_v2():
    """
    Print 12345 on 5 rows (version 2).
    """
    print(pattern_02_v2.__name__)
    print(pattern_02_v2.__doc__.lstrip().rstrip())
    for row in range(5):
        print('12345')
    print()

def pattern_03():
    """
    Print 5 lines of 1, 2, ..., 5.
    """
    print(pattern_03.__name__)
    print(pattern_03.__doc__.lstrip().rstrip())
    for row in range(1, 6):
        for column in range(5):
            print(row, end = '')
        print()
    print()

def pattern_04():
    """
    Print 5 lines of A, B, ..., E.
    """
    print(pattern_04.__name__)
    print(pattern_04.__doc__.lstrip().rstrip())
    for row in 'ABCDE':
        for column in range(5):
            print(row, end = '')
        print()
    print()

def pattern_05():
    """
    Print ABCDE on 5 rows.
    """
    print(pattern_05.__name__)
    print(pattern_05.__doc__.lstrip().rstrip())
    for row in range(5):
        for column in 'ABCDE':
            print(column, end = '')
        print()
    print()

def pattern_06():
    """
    Print tbd
    """
    print(pattern_06.__name__)
    print(pattern_06.__doc__.lstrip().rstrip())
    for row in range(5):
        for column in 'ABCDE':
            print(column, end = '')
        print()
    print()

def pattern_07():
    """
    Print tbd
    """
    pass

def pattern_08():
    """
    Print tbd
    """
    pass

def pattern_09():
    """
    Print tbd
    """
    pass

def pattern_10():
    """
    Print tbd
    """
    pass

if __name__ == '__main__':
    pattern_01()
    pattern_02()
    pattern_02_v2()
    pattern_03()
    pattern_04()
    pattern_05()
    pattern_06()
    pattern_07()
    pattern_08()
    pattern_09()
    pattern_10()
