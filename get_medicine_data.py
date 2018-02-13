#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

import sys
sys.path.append('../../anamnese/')
import django
import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'anamnese.settings'
django.setup()
from knowledge_database.models import Medicine
from neomodel import config, db
config.DATABASE_URL = 'bolt://neo4j:123456@localhost:7687' 
db.set_connection('bolt://neo4j:123456@127.0.0.1:7687')
import datetime



def get_data(filename, format = 'str', splitlines = False):
    """
    Return filename content in specified format. Manage exceptions: file presence, access mode and other.
    """
    unsupported_format_error_message = "Sorry, we handle only the following formats: 'json','str'(default)."

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

def database_medicine_file(input_filename):
    """
    Read medicine file and database medicine data.
    """
    medicine_lines = get_data(input_filename, splitlines = True)
    error_medicine_data = []
    for line in medicine_lines:
        try:
            value_list = line.split(sep = '\t')
            commercial_name = Medicine(
                name = value_list[1],
                updated_by = 'cod',
                CIS_code = value_list[0],
                commercial_name = value_list[1],
                pharmaceutical_form = value_list[2],
                routes = value_list[3],
                amm_status = value_list[4],
                amm_procedure_type = value_list[5],
                marketing_status = value_list[6],
                amm_date = datetime.datetime.strptime(value_list[7], '%d/%m/%Y').date(),
                bdm_status = value_list[8],
                european_authorization_number = value_list[9],
                holders = value_list[10],
                reinforced_surveillance = value_list[11]).save()
        except Exception as exception_other:
            print(exception_other)
            print(line)
            error_medicine_data.append(line)

def database_generics_file(input_filename):
    """
    Read generics file and database generics  data.
    """
    generic_lines = get_data(input_filename, splitlines = True)
    generic_data_error = []
    number_unfound = 0
    for generic_line in generic_lines:
        try:
            value_list = generic_line.split(sep = '\t')
            try:
                medicine_found = Medicine.nodes.get(CIS_code = value_list[2])
                medicine_found.alternative_name = value_list[1]
                medicine_found.save()
            except Medicine.DoesNotExist:
                number_unfound += 1
        except Exception as exception_other:
            print(exception_other)
            print(generic_line)
            generic_data_error.append(generic_line)
        finally:
            pass
    print('number unfound:', number_unfound)

if __name__ == '__main__':
    medicine_filename       = 'CIS_bdpm.txt'
    medicine_error_filename = 'CIS_bdpm_error.txt'
    generics_filename       = 'CIS_GENER_bdpm.txt'
    generics_error_filename = 'CIS_GENER_bdpm_error.txt'
    database_medicine_file(medicine_filename)
    database_generics_file(generics_filename)
