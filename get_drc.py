#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

import sys
sys.path.append('../../anamnese/')
import django
import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'anamnese.settings'
django.setup()
from knowledge_database.models import Cluster
from neomodel import config, db
config.DATABASE_URL = 'bolt://neo4j:123456@localhost:7687' 
db.set_connection('bolt://neo4j:123456@127.0.0.1:7687')
import baz_utilities as baz
sys.path.append('../icd_10/')
import distances


def filled_rc_criterion_dict(rc_criterion_filename, rc_criterion_dict_error_filename):
    """
    Returns a dictionary extracted from rc_criterion_filename: {key = rc, value = set of linked criteria}.
    Stores errors in rc_criterion_dict_error_filename.
    :rtype: dict
    """
    rc_criterion_lines = baz.get(rc_criterion_filename, splitlines = True)
    rc_criterion_dict = {}
    rc_criterion_dict_error_lines = []
#    for rc_criterion_line in rc_criterion_lines[1:]:
    for line_index, rc_criterion_line in enumerate(rc_criterion_lines[1:], start = 1):
        try:
            rc_criterion_line_items = rc_criterion_line.split('\t')
            rc_id     = rc_criterion_line_items[1]
            criterion = rc_criterion_line_items[7]
            try:
                rc_criterion_dict[rc_id].add(criterion)
            except:
                rc_criterion_dict[rc_id] = set()
                rc_criterion_dict[rc_id].add(criterion)
        except Exception as exception_other:
            print('line index:', line_index, '   ', exception_other, ':', rc_criterion_line)
            rc_criterion_dict_error_lines.append(('line index: ', line_index, rc_criterion_line))
    baz.put(rc_criterion_dict_error_lines, rc_criterion_dict_error_filename, format = 'json')
    return rc_criterion_dict


def filled_rc_icd10_dict(rc_icd10_filename, rc_icd10_dict_error_filename):
    """
    Returns a dictionary extracted from rc_icd10_filename: {key = rc, value = set of linked icd10 codes}.
    Stores errors in rc_icd10_dict_error_filename.
    :rtype: dict
    """
    rc_icd10_lines = baz.get(rc_icd10_filename, splitlines = True)
    rc_icd10_dict = {}
    rc_icd10_dict_error_lines = []
    for rc_icd10_line in rc_icd10_lines[1:]:
        try:
            rc_icd10_line_items = rc_icd10_line.split('\t')
            rc_id = rc_icd10_line_items[1]
            icd10_code_1 = rc_icd10_line_items[2]
            icd10_code_2 = rc_icd10_line_items[6]
            try:
                rc_icd10_dict[rc_id].add(icd10_code_1)
                rc_icd10_dict[rc_id].add(icd10_code_2)
            except:
                rc_icd10_dict[rc_id] = set()
                rc_icd10_dict[rc_id].add(icd10_code_1)
                rc_icd10_dict[rc_id].add(icd10_code_2)
        except Exception as exception_other:
            print(exception_other, ':', rc_icd10_line)
            rc_icd10_dict_error_lines.append(rc_icd10_line)
    baz.put(rc_icd10_dict_error_lines, rc_icd10_dict_error_filename, format = 'json')
    return rc_icd10_dict


def update_cluster_from_drc(icd10_id):
    """
    Update cluster from icd10 codes found in drc.
    """
    try:
        cluster_found = Cluster.nodes.get(icd10_id = icd10_id)
        cluster_found.is_in_drc = True
        cluster_found.updated_by = 'update_cluster_from_drc'
        cluster_found.save()
    except Exception as exception_other:
        print('ICD10 cluster referenced in DRC but not found in neo4j:', exception_other)
    return


def most_relevant_clusters(clusters):
    """
    Returns the clusters that must receive drc criteria.
    :param cluster_list: list of cluster ids
    :return: list of most numerous cluster prefixes
    """
    # the selection algo is based on the number of occurrences; this may be improved
    # an icd10 code is formed by: a prefix LXY, a point '.' and a suffix 'ZT', with L being a letter and XYZT figures.
    cluster_list = list(clusters)
    if len(cluster_list) == 0:
        return
    elif len(cluster_list) == 1:
        return cluster_list[0]
    else:
        # make a list of all prefixes and their number of occurrence
        cluster_prefix_number_dict = {}
        clusters_chosen = []
        for cluster in cluster_list:
            cluster_prefix = baz.unquoted(cluster).split(sep = '.', maxsplit = 1)[0]
            try:
                cluster_prefix_number_dict[cluster_prefix] += 1
            except:
                cluster_prefix_number_dict[cluster_prefix] = 1
        #baz.put_debug('cluster_prefix_number_dict', cluster_prefix_number_dict)
        max_number = max(cluster_prefix_number_dict.values())
        #baz.put_debug('max_number', max_number)
        for cluster_prefix in cluster_prefix_number_dict.keys():
            #baz.put_debug('cluster_prefix', cluster_prefix)
            if cluster_prefix_number_dict[cluster_prefix] == max_number:
                clusters_chosen.append(cluster_prefix)
        #baz.put_debug('clusters_chosen', clusters_chosen)
        return clusters_chosen


def database_drc(rc_icd10_filename, rc_criterion_filename):
    """
    Read resultat de consultation (rc) file and include missing items in neo4j.
    rc is diagnostic.
    criterion is condition for rc: either criterion must be present, or must be absent, or n criteria among p must be present.
    """
    # create a dictionary which returns the set of criterion linked to an rc
    rc_criterion_dict = filled_rc_criterion_dict(rc_criterion_filename, rc_criterion_dict_error_filename)
    baz.put_debug('rc_criterion_dict', rc_criterion_dict, type_id = False)
    # create a dictionary which returns the set of icd10 codes linked to an rc
    rc_icd10_dict     = filled_rc_icd10_dict (rc_icd10_filename, rc_icd10_dict_error_filename)
    baz.put_debug('rc_icd10_dict', rc_icd10_dict, type_id = False)
    # update neo4j existing and missing nodes with drc
    rc_icd10_lines = baz.get(rc_icd10_filename, splitlines = True)
    database_drc_error_lines = []
    for rc_icd10_line in rc_icd10_lines[1:]:
        try:
            rc_icd10_line_items = rc_icd10_line.split(sep = '\t')
            # update first (principal) icd10 code from drc
            icd10_code_1 = baz.unquoted(rc_icd10_line_items[2])
            update_cluster_from_drc(icd10_code_1)
            # update second (additional) icd10 code from drc
            icd10_code_2 = baz.unquoted(rc_icd10_line_items[6])
            update_cluster_from_drc(icd10_code_2)
        except Exception as exception_other:
            print(exception_other, ':', rc_icd10_line)
            database_drc_error_lines.append(rc_icd10_line)
    baz.put(database_drc_error_lines, database_drc_error_filename, format = 'json')

    # update clusters with missing criteria
    for rc in rc_icd10_dict.keys():
        clusters_to_update = most_relevant_clusters(rc_icd10_dict[rc])
        baz.put_debug('clusters_to_update', clusters_to_update)
        criteria_to_update = rc_criterion_dict[rc]
        baz.put_debug('criteria_to_update', criteria_to_update)
        for cluster in clusters_to_update:
            try:
                cluster_found = Cluster.nodes.get(icd10_id = cluster)
                print('ICD10 cluster referenced in DRC and found in neo4j:', cluster)
            except:
                print('ICD10 cluster referenced in DRC but not found in neo4j:', cluster)
            # criteria_existing = tbd
        # decide what to do
    return


if __name__ == '__main__':
    # initialize all clusters as not in drc
    db.cypher_query("match (c:Cluster) set c.is_in_drc = False return c")
#    rc_icd10_filename                = 'ref_l_rc_cim10_test.txt'
#    rc_criterion_filename            = 'ref_definition_test.txt'
#    rc_criterion_dict_error_filename = 'rc_criterion_dict_error_test.txt'
#    rc_icd10_dict_error_filename     = 'rc_icd10_dict_error_test.txt'
#    database_drc_error_filename      = 'database_drc_error_test.txt'
#    drc_criteria_not_in_neo4j        = 'drc_criteria_not_in_neo4j_test.txt'
    rc_icd10_filename                = 'ref_l_rc_cim10.txt'
    rc_criterion_filename            = 'ref_definition.txt'
    rc_criterion_dict_error_filename = 'rc_criterion_dict_error.txt'
    rc_icd10_dict_error_filename     = 'rc_icd10_dict_error.txt'
    database_drc_error_filename      = 'database_drc_error.txt'
    drc_criteria_not_in_neo4j        = 'drc_criteria_not_in_neo4j.txt'
    database_drc(rc_icd10_filename, rc_criterion_filename)
