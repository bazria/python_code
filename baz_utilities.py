#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

import json

unsupported_format_error_message = "Sorry, we handle only the following formats: 'json','str'(default)."

def get_data(filename, format = 'str', splitlines = False):
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
        print('File not found: %s' % (filename))
    except PermissionError:
        print('File not in read mode: %s' % (filename))
    except Exception as exception_other:
        print('File error: %s' % (filename))
        print(exception_other)

def put_data(content, filename, format = 'str', indent = 0):
    """
    Write content into filename in specified format. Manage exception.
    """
    try:
        with open(filename, 'w') as output_file:
            if format == 'json':
                # CAUTION: setting ensure_ascii = True prevents from writing properly accents
                json.dump(obj = content, fp = output_file, ensure_ascii = False, indent = indent)
            elif format == 'str':
                output_file.write(str(content))
            else:
                raise Exception(unsupported_format_error_message)
    except Exception as exception_other:
        print('File error: %s' % (filename))

def put_debug(variable_name, variable, type_id = True):
    """
    Print variable name, value, type and id for debugging purposes.
    """
    print('------------------------------')
    print('variable name :', variable_name)
    if type_id:
        print('variable type :', type(variable))
        print('variable id   :', id(variable))
    print('variable value:', variable)
    print('------------------------------')

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

def unquoted_old_todelete(string):
    """
    Remove enclosing simple or double quotes.
    Old version to delete, remove only one level of enclosing.
    """
    try:
        if (string.startswith('"') and string.endswith('"')):
            return(string.lstrip('"').rstrip('"'))
        elif (string.startswith("'") and string.endswith("'")):
            return(string.lstrip("'").rstrip("'"))
    except:
        return(string)

def test_unquoted_old_todelete():
    variable = "test 00: string variable"
    print(variable)
    print(unquoted_old_todelete(variable))
    print(unquoted_old_todelete('test 01: simple quotes'))
    print(unquoted_old_todelete("test 02: double quotes"))
    print(unquoted_old_todelete("'test 03: double, simple quotes'"))
    print(unquoted_old_todelete('"test 04: simple, double quotes"'))
    print(unquoted_old_todelete("""""test 05: 5 double quotes"""""))
    print(unquoted_old_todelete('''''test 06: 5 simple quotes'''''))
    print(unquoted_old_todelete("'"'"test 07: 5 alternate double & simple quotes"'"'"))
    print(unquoted_old_todelete('"'"'test 08: 5 alternate double & simple quotes'"'"'))
    print(unquoted_old_todelete('123'))
    print(unquoted_old_todelete("123"))
    print(unquoted_old_todelete('''123'''))
    print(unquoted_old_todelete("""123"""))

if __name__ == '__main__':
    """
    When run as a script, execute module tests.
    """

    test_unquoted()
    test_unquoted_old_todelete()
#    test_get_data()
#    test_put_data()
#    test_put_debug()
# tests for unquoted
#    put_debug('content', get_data('baz_utilities_testdata_in_00.txt', format = 'mp9'))
#    put_data('test data', 'baz_utilities_testdata_out_json.txt', format = 'json', indent = 4)
#    put_data('test data', 'baz_utilities_testdata_out_str.txt', format = 'str')
