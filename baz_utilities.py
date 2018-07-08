#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

import json
import os

unsupported_format_error_message = "Sorry, we handle only the following formats: 'json','str'(default)."


def normalized_filename(filename):
    """
    Renames file in order to make it 'safe' with respect to any filesystem.
    Files starting by the character '.' (dot) are left unchanged as they usually represent system files.
    Actually replaces each character not allowed by an equivalent allowed character.  For example:
    - ' ' is replaced by '_',
    - 'é' is replaced by 'e',
    - 'A' is replaced by 'a'.
    - uppercase are replaced by lowercases,
    - accentuated characters are replaced by their unaccentuated counterpart,
    - spaces are deleted,
    - tbd raises all paths above predefined lengths
    TODO TBD:
    - file starting by space,
    """
    letters_allowed = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',\
                       't', 'u', 'v', 'w', 'x', 'y', 'z'}
    numbers_allowed = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
    symbols_allowed = {'_', '.'}
    characters_allowed = frozenset(letters_allowed.union(numbers_allowed, symbols_allowed))
    e_accentuated = {'é', 'è', 'ê'}
    # leave system files unchanged
    if filename.startswith('.'):
        return filename
    else:
        normalized_filename = filename.lower()
        for character in filename:
            if character in characters_allowed:
                normalized_filename = ''.join(character)
            #elif character in e_accentuated:
                #pass
        return normalized_filename


def normalize_filenames(directory):
    """
    Normalizes all filenames in given directory.
    :param directory:
    :return:
    todo tbd:
    - option --U:          leave uppercase characters unchanged,
    - option --dry-run:    do everything except rename the file.  Recommended to estimate execution time.
    - option --verbose:    print each change made.  Compatible with --dry-run,
    - option --underscore: replace whitespace by underscore ('_')  (default),
    - option --dash:       replace whitespace by dash ('-'),
    - option --nothing:    replace whitespace by no character (''),
    - option --one:        replace consecutive whitespaces by one replacing character,
    - option --keep-ws-nb: replaces consecutive whitespaces by the same number of replacing characters (default).
    - print begin and end times
    """
    print(directory)
    # walk recursively directory


def get(filename, format = 'str', splitlines = False):
    """
    Return filename content in specified format. Manage exceptions: file presence, access mode and other.
    """
    try:
        with open(filename, 'r', encoding ='ISO-8859-1') as input_file:
            if format == 'json':
                return json.load(input_file)
            elif format == 'str':
                if splitlines:
                    return input_file.read().splitlines()
                else:
                    return input_file.read()
            else:
                raise Exception(unsupported_format_error_message)
    except FileNotFoundError:
        print('    File not found: %s' % filename)
    except PermissionError:
        print('    File not in read mode: %s' % filename)
    except Exception as exception_other:
        print('    File error: %s' % filename)
        print(exception_other)

def put(content, filename, format = 'str', indent = 0):
    """
    Write content into filename in specified format. Manage exception.
    """
    try:
        with open(filename, 'w') as output_file:
            # if content is not empty, write it in the file
            if content:
                if format == 'json':
                    # CAUTION: setting ensure_ascii = True prevents from writing properly accents
                    json.dump(obj = content, fp = output_file, ensure_ascii = False, indent = indent)
                elif format == 'str':
                    output_file.write(str(content))
                else:
                    raise Exception(unsupported_format_error_message)
            # if content is empty, write an empty file to ease immediate visual check
            else:
                pass
    except Exception as exception_other:
        print('    File error: %s' % filename)

def put_debug(variable_name, variable, type_id = False):
    """
    Print variable name, value, type and id for debugging purposes.
    """
    print('begin------------------------------')
    print('variable name :', variable_name)
    if type_id:
        print('variable type :', type(variable))
        print('variable id   :', id(variable))
    print('variable value:', variable)
    print('end------------------------------')

def unquoted(string):
    """
    Remove as many pairs of enclosing quotes (simple or double) as possible.
    """
    try:
        if (string.startswith('"') and string.endswith('"')):
            return unquoted(string.lstrip('"').rstrip('"'))
        elif (string.startswith("'") and string.endswith("'")):
            return unquoted(string.lstrip("'").rstrip("'"))
        else:
            return(string)
    except:
        return(string)

def test_unquoted():
    variable = "test 00: string variable"
    print(variable)
    print(unquoted(variable))
    print(unquoted('test 01: simple quotes'))
    print(unquoted("test 02: double quotes"))
    print(unquoted("'test 03: double, simple quotes'"))
    print(unquoted('"test 04: simple, double quotes"'))
    print(unquoted("""""test 05: 5 double quotes"""""))
    print(unquoted('''''test 06: 5 simple quotes'''''))
    print(unquoted("'"'"test 07: 5 alternate double & simple quotes"'"'"))
    print(unquoted('"'"'test 08: 5 alternate double & simple quotes'"'"'))
    print(unquoted('123'))
    print(unquoted("123"))
    print(unquoted('''123'''))
    print(unquoted("""123"""))

def secured_str(string):
    """
    Returns a string that can be used as a string without any further precaution regarding presence of internal simple,
    double quotes, apostrophe, etc.
    tbd baz
    :param string:
    :return:
    """

if __name__ == '__main__':
    """
    When run as a script, execute module tests.
    """
    filename_system = """.l'abricOt est dans l'école et la grève"""
    filename_test01 = """l'abricOt est dans l'école et la grève"""
    print(filename_system)
    print(normalized_filename(filename_system))
    print(filename_test01)
    print(normalized_filename(filename_test01))
    # todo tbd use unittest
#    test_unquoted()
#    test_get()
#    test_put()
#    test_put_debug()
# tests for unquoted
#    put_debug('content', get('baz_utilities_testdata_in_00.txt', format = 'mp9'))
#    put('test data', 'baz_utilities_testdata_out_json.txt', format = 'json', indent = 4)
#    put('test data', 'baz_utilities_testdata_out_str.txt', format = 'str')
