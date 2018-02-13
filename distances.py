from Levenshtein import *
import matplotlib.pyplot as plt
import numpy as np
import sys
sys.path.append("../../anamnese/")
sys.path.append("../general/")
import django
import os
os.environ["DJANGO_SETTINGS_MODULE"] = "anamnese.settings"
django.setup()
from neomodel import config, db
from knowledge_database.models import Cluster, Indication, MedicalHistory, Symptom, RiskFactor
from cosine import distance_cosine
config.DATABASE_URL = "bolt://neo4j:123456@localhost:7687"
db.set_connection("bolt://neo4j:123456@127.0.0.1:7687")


def cleaned_criteria(line):
    """
    Returns a text-only casefolded string criteria without leading and trailing clutter.
    """
    if '"' in line:
        return line.split('"')[1].rstrip().casefold().replace('1ère', 'première').replace('1re', 'première').replace('1er', 'premier').replace('2ème', 'deuxième').replace('2e', 'deuxième').strip(' \t-+|123456789')


def filled_distance_table(number_of_indications, number_of_criteria, indication_list, criteria_list, distance_model):
    """
    Returns a table containing the distance between the indication (line index) and the criteria (column index) computed according to distance_model.
    """
    # initialize table
    filled_distance_table = np.ones((number_of_indications, number_of_criteria))
    # populate table
    for indication_index in range(number_of_indications):
        if indication_index % 20 == 0:
            print('Processing indication number:', indication_index)
        for criteria_index in range(number_of_criteria):
            filled_distance_table[indication_index, criteria_index] = distance_model(str(indication_list[indication_index].name).casefold(), str(criteria_list[criteria_index]))
    return filled_distance_table


def closest_indication_index_to(number_of_indications, criterion_index, distance_table):
    """
    Returns the index of the indication which has the minimal distance with criterion_index.
    """
    indication_index_of_minimal_distance = 0
    for indication_index in range(number_of_indications):
        if distance_table[indication_index, criterion_index] < distance_table[indication_index_of_minimal_distance, criterion_index]:
            indication_index_of_minimal_distance = indication_index
    return indication_index_of_minimal_distance


def find_closest_indication():
    medical_history_list = MedicalHistory.nodes.all()
    symptom_list = Symptom.nodes.all()
    risk_factor_list = RiskFactor.nodes.all()
    indication_list = []
    indication_list.extend(medical_history_list)
    indication_list.extend(symptom_list)
    indication_list.extend(risk_factor_list)
    number_of_indications = len(indication_list)
    with open('ref_definition.txt','r', encoding='ISO-8859-1') as rc_criteria_file:
        rc_criteria_lines = rc_criteria_file.readlines()[11:]
    clean_criteria_set = set()
    for rc_criteria_line in rc_criteria_lines:
        if cleaned_criteria(rc_criteria_line):
            clean_criteria_set.add(cleaned_criteria(rc_criteria_line))
    number_of_unique_criteria = len(clean_criteria_set)
    clean_criteria_list = list(clean_criteria_set)
    criteria_clean_filename = 'criteria_clean.txt'
    print()
    print('Computing Levenshtein distances ...')
    levenshtein_distance_table = filled_distance_table(number_of_indications, number_of_unique_criteria, indication_list, clean_criteria_list, distance)
    selected_distance_table = levenshtein_distance_table
    print()
    #print('Computing cosine distances ...')
    #cosine_distance_table      = filled_distance_table(distance_model = distance_cosine)
    # select below the distance model to be used: distance (Levenshtein) or distance_cosine
    #selected_distance_table = cosine_distance_table
    closest_indication_index_list = [0 for i in range(number_of_unique_criteria)]
    closest_distance_list = [0 for i in range(number_of_unique_criteria)]
    for criterion_index in range(number_of_unique_criteria):
        closest_indication_index = closest_indication_index_to(number_of_indications, criterion_index, selected_distance_table)
        closest_indication_index_list[criterion_index] = closest_indication_index
        closest_distance_list[criterion_index] = selected_distance_table[closest_indication_index, criterion_index]
    closest_indication_list = []
    for criterion_index in range(number_of_unique_criteria):
        # for COSINE distance, the suggested threshold is 0.15
        # if closest_distance_list[criterion_index] < 0.15:
        # for LEVENSHTEIN distance, choose distance threshold (we suggest <= 1) and make sure that the first character is the same (very discriminant)
        if (closest_distance_list[criterion_index] <= 1) and (clean_criteria_list[criterion_index][0] == indication_list[closest_indication_index_to(number_of_indications, criterion_index, selected_distance_table)].name.casefold()[0]):
#            print(clean_criteria_list[criterion_index])
#            print(indication_list[closest_indication_index_to(number_of_indications, criterion_index, selected_distance_table)].name.casefold())
            closest_indication_list.append((clean_criteria_list[criterion_index], indication_list[closest_indication_index_to(number_of_indications, criterion_index, selected_distance_table)].name.casefold()))
    #plt.hist(closest_distance_list)
    #plt.show()
    return clean_criteria_list, closest_indication_list


if __name__ == '__main__':
    clean_criteria_list, closest_indication_list = find_closest_indication()
    indication_found = set()
    for indications in closest_indication_list:
        indication_found.add(indications[0])
        indication_found.add(indications[1])
    number_of_added_criteria = 0
    for criterion in clean_criteria_list:
        if criterion not in indication_found:
            new_indication = Symptom(name       = criterion,
                                     updated_by = 'drc_criteria').save()
            number_of_added_criteria += 1
    print('Number of criteria added:', number_of_added_criteria)
