#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

import itertools
import json
import os
import unittest

unsupported_format_error_message = "Sorry, we handle only the following formats: 'json','str'(default)."
lowercase_letters_safe = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                          'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'}
uppercase_letters_safe = {'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                          'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'}
digits_safe = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
symbols_safe = {'.', '_', '-'}
characters_posix_safe = frozenset(symbols_safe.union(uppercase_letters_safe, lowercase_letters_safe, digits_safe))
# todo tbd understand this
accents = dict(zip('ÂÃÄÀÁÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖØÙÚÛÜÝÞßàáâãäåæçèéêëìíîïðñòóôõöøùúûüýþÿ',
   itertools.chain('AAAAAA', ['AE'], 'CEEEEIIIIDNOOOOOOUUUUYP', ['ss'],
                   'aaaaaa', ['ae'], 'ceeeeiiiionoooooouuuuypy')))
# todo tbd try to make a string.translate or any other method


def safe_character(character):
    """
    Returns an equivalent safe character with respect to POSIX filename requirements.
    :param character: input character of unknown safety.
    :return: corresponding safe character, empty if unavailable.
    Actually replaces each unsafe character by its safe equivalent.  For example:
    - accentuated characters are replaced by their unaccentuated counterpart, eg 'é' by 'e', 'À' by 'A',
    - spaces, unsafe symbols are replaced by an empty string.
    """
    # if the character is safe (most common case), return it
    if character in characters_posix_safe:
        return character
    # else if the character is accentuated, return its unaccentuated counterpart
    elif character in accents:
        return accents[character]
    # in all other cases, return an empty string
    else:
        return ''


def safe_filename(in_filename, force_lowercase=False, force_uppercase=False):
    """
    Returns a corresponding safe filename with respect to POSIX filename requirements.
    :param in_filename: input filename of unknown safety.
    :param force_lowercase:
    :param force_uppercase:
    :return: corresponding safe filename.
    Files starting by the character '.' (dot) are left unchanged as they usually represent system files.
    TODO TBD:
    # todo tbd add tests as in source file
    - file starting by space, '-', '_'
    - check that filename is not empty, otherwise name 'rnmd_abcdefg', as for duplicates
    """
    # leave system files unchanged
    if in_filename.startswith('.'):
        return in_filename
    else:
        out_filename = ''
        for character in in_filename:
            out_filename += ''.join(safe_character(character))
        if force_lowercase:
            return out_filename.lower()
        elif force_uppercase:
            return out_filename.upper()
        else:
            return out_filename


def normalize_filenames(top_directory, max_depth):
    """
    Renames files in given directory in order to make them 'safe' with respect to POSIX filename requirements.
    :param top_directory: top directory to process.
    :return: max_depth.
    todo tbd options:
    -c --uppercase:    force uppercase,
    -d --dash:         replace whitespace by dash ('-'),
    -e --empty:        replace whitespace by empty string (''),
    -k --keep:         replace consecutive whitespaces by the same number of replacing characters (default),
    -l --lowercase:    force lowercase,
    -o --one:          replace consecutive whitespaces by one replacing character,
    -r --recursive:    process recursively all subdirectories.
    -s --show:         print replaced characters and their replacing character, according to passed options,
    -t --time:         print begin and end times,
    -u --underscore:   replace whitespace by underscore ('_'),
    -v --verbose:      for each file, print initial and safe names.  Compatible with --dry-run,
    -y --dry-run:      do everything except rename the file,
    """
    for root, directories, files in os.walk(top_directory):
        print
        for file in files:
            print(file)
#            if ".docx" in file:
#                print(os.path.join(r, file))


def get(filename, format='str', splitlines = False):
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
#    print(accents)
#    filename_test00 = """.l'abricOt est dans l'école et la grève"""
#    filename_test01 = """l'abricOt est dans l'école et la grève"""
#    print(filename_test00)
#    print(safe_filename(filename_test00))
#    print(filename_test01)
#    print(safe_filename(filename_test01))
#    print(safe_character(' '))
#    print(safe_character('à'))
#    print(safe_character('^'))
#    print(safe_character('¨'))
    max_depth = 0
    normalize_filenames('test_dir0', max_depth)
    # todo tbd use unittest
#    test_unquoted()
#    test_get()
#    test_put()
#    test_put_debug()
# tests for unquoted
#    put_debug('content', get('baz_utilities_testdata_in_00.txt', format = 'mp9'))
#    put('test data', 'baz_utilities_testdata_out_json.txt', format = 'json', indent = 4)
#    put('test data', 'baz_utilities_testdata_out_str.txt', format = 'str')
