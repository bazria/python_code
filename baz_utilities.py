#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

import json
import itertools
import os

unsupported_format_error_message = "Sorry, we handle only the following formats: 'json','str'(default)."
lowercase_allowed = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', \
                     't', 'u', 'v', 'w', 'x', 'y', 'z'}
uppercase_allowed = {'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', \
                     'T', 'U', 'V', 'W', 'X', 'Y', 'Z'}
numbers_allowed = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
symbols_allowed = {'_', '.'}
characters_allowed = frozenset(lowercase_allowed.union(numbers_allowed, symbols_allowed))
characters_allowed_upper = frozenset(characters_allowed.union(uppercase_allowed))


def safe(character):
    accents = dict(zip('ÂÃÄÀÁÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖØÙÚÛÜÝÞßàáâãäåæçèéêëìíîïðñòóôõöøùúûüýþÿ',
                        itertools.chain('AAAAAA', ['AE'], 'CEEEEIIIIDNOOOOOOUUUUYP', ['ss'],
                                        'aaaaaa', ['ae'], 'ceeeeiiiionoooooouuuuypy')))
    # try to make a string.translate
    #todo add tests as in source file
    if character in accents:
        return accents[character]
    if ord(character) < 32 or ord(character) == 127 or character not in characters_allowed_upper:
        return ''
    else:
        return character


def normalized(filename, *options):
    """
    Returns a normalized filename.
    Files starting by the character '.' (dot) are left unchanged as they usually represent system files.
    Actually replaces each character not allowed by an equivalent allowed character.  For example:
    - ' ' is replaced by '_',
    - 'é' is replaced by 'e',
    - 'A' is replaced by 'a'.
    - uppercase are replaced by lowercases,
    - accentuated characters are replaced by their unaccentuated lowercase counterpart,
    - spaces are deleted,
    - tbd raises all paths above predefined lengths
    TODO TBD:
    - file starting by space,
    """
    force_lower = False
    # leave system files unchanged
    if filename.startswith('.'):
        return filename
    else:
        filename_normalized = ''
        for character in filename:
            if character in characters_allowed:
                filename_normalized += ''.join(character)
            else:
                pass
        if force_lower:
            return filename.lower()
        return filename_normalized


def normalize_filenames(directory):
    """
    Renames files in given directory in order to make it 'safe' with respect to any filesystem.
    :param directory: top directory to process.
    :return: None.
    todo tbd options:
    -n --nonrecursive: process only given directory.
    -U --uppercase:    leave uppercase characters unchanged,
    -d --dry-run:      do everything except rename the file.  Recommended to estimate execution time,
    -v --verbose:      for each file, print initial and final names.  Compatible with --dry-run,
    -u --underscore:   replace whitespace by underscore ('_')  (default),
    -d --dash:         replace whitespace by dash ('-'),
    -n --nothing:      replace whitespace by no character (''),
    -o --one:          replace consecutive whitespaces by one replacing character,
    -k --keep:         replace consecutive whitespaces by the same number of replacing characters (default),
    -t --time:         print begin and end times,
    -s --show:         print replaced characters and their replacing character, according to passed options,
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
    Returns a string that can be used as a string without any further precaution regarding presence of simple,
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
    print(normalized(filename_system))
    print(filename_test01)
    print(normalized(filename_test01))
    print(safe('à'))
    print(safe('^'))
    print(safe('¨'))
    # todo tbd use unittest
#    test_unquoted()
#    test_get()
#    test_put()
#    test_put_debug()
# tests for unquoted
#    put_debug('content', get('baz_utilities_testdata_in_00.txt', format = 'mp9'))
#    put('test data', 'baz_utilities_testdata_out_json.txt', format = 'json', indent = 4)
#    put('test data', 'baz_utilities_testdata_out_str.txt', format = 'str')
