#!/usr/local/bin/python3
# -*- coding: utf-8 -*-


import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'anamnese.settings'

import django
django.setup()

from neomodel import config, db
config.DATABASE_URL = 'bolt://neo4j:123456@localhost:7687'
db.set_connection('bolt://neo4j:123456@127.0.0.1:7687')

from django.test import TestCase
from knowledge_database import cypherService

import matplotlib.pyplot as plt
import inspect


def put_test(node_uids, node_name, testing):
    """
    Print formatted variables only if testing.
    :return:  None
    """
    if testing:
        print('   ', node_name, 'uids :', node_uids)
        print('   ', node_name, 'count:', len(node_uids))
        print()

def inner_node_uids(data):
    """
    Returns list of node uids found by get_diagnostic.
    """
    return [data[node][0].properties['uid'] for node in range(len(data))]

def diagnostic_algorithm_00(node_uids, testing=False):
    """
    Wrap function get_diagnostic to standardize test inputs and outputs.
    """
    return inner_node_uids(cypherService.get_diagnostic(node_uids))

def diagnostic_algorithm_01(node_uids, testing=False):
    """
    Return node uids of nodes directly related to argument node uid by adaptatively de-discriminating inclusive scope.
    """

    queries = [
        "match (node:Cluster)-[:is_caused_by               ]-(nodes) where nodes.uid in {node_uids} return distinct node.uid limit 3",
        "match (node:Cluster)-[:             has_expression]-(nodes) where nodes.uid in {node_uids} return distinct node.uid limit 3",
        "match (node:Cluster)-[                            ]-(nodes) where nodes.uid in {node_uids} return distinct node.uid limit 3",
        "match (node        )-[                            ]-(nodes) where nodes.uid in {node_uids} return distinct node.uid limit 3",
    ]
    for index, query in enumerate(queries):
        data, label = db.cypher_query(queries[index], {'node_uids': node_uids})
        if data:
            node_found_uids = [item[0] for item in data]
            put_test(node_found_uids, 'Node found', testing)
            if testing:
                print('    Index:', index)
            return node_found_uids
    print('    No cluster found ----------------------------------------------------------------------------------')
    print('    for nodes:', node_uids)
    return []


class test_scenario_class(TestCase):
    """
    Test behavior of application knowledge_database through typical scenarios.
    """

    def test_diagnostic_algorithms(self):
        """
        Test diagnostic algorithms.
        :return:  None
        """

        diagnostic_algorithm_results = {
            diagnostic_algorithm_00:
                {
                    'name'              : 'diagnostic_algorithm_00',
                    #tbdbaz to factor
                    'node_syndrome_uids': [],
                    'node_found_uids'   : [],
                },
            diagnostic_algorithm_01:
                {
                    'name'              : 'diagnostic_algorithm_01',
                    #tbdbaz to factor
                    'node_syndrome_uids': [],
                    'node_found_uids'   : [],
                },
        }
        node_syndrome_testing  = False
        # uncomment following line to run test mode
        node_syndrome_testing = [47100, 47103, 46663, 46664, 46665]
        # nodes 47100, 47103 correspond to grippe
        # nodes 46663, 46664, 46665 correspond to angine de poitrine

        # get nodes syndrome
        print()
        print()
        print('    Testing diagnostic algorithms:')
        print()
        if not node_syndrome_testing:
            print('    Real mode')
            query = "match (node)-[: is_caused_by | has_expression]-() where node.tag='syndrome' return distinct node.uid"
            data, label = db.cypher_query(query)
            node_syndrome_uids = [item[0] for item in data]
        else:
            print('    Test mode')
            node_syndrome_uids = [str(element) for element in node_syndrome_testing]
        node_syndrome_count = len(node_syndrome_uids)
        put_test(node_syndrome_uids, 'Node syndrome', node_syndrome_testing)

        # get number of symptoms related to each node syndrome
        number_symptoms_per_syndrome = []
        for node_syndrome_uid in node_syndrome_uids:
            query = "match (syndrome)-[:is_caused_by|has_expression]-(symptoms) where syndrome.uid=" + "'" + str(node_syndrome_uid) + "'" + " return distinct count (symptoms)"
            data, label = db.cypher_query(query)
            number_symptoms = data[0][0]
            number_symptoms_per_syndrome.append(number_symptoms)

        # get nodes related to node syndrome
        print('    Processing node syndrome count: (out of ', node_syndrome_count, ')', sep='')
        for index, node_syndrome_uid in enumerate(node_syndrome_uids, start=1):
            if (index % 10) == 0:
                print(index, end='...  ', flush=True)
            query = "match (node)-[: is_caused_by | has_expression]-(nodes) where node.uid=" + "'" + str(node_syndrome_uid) + "'" + " return distinct nodes.uid"
            data, label = db.cypher_query(query)
            node_related_uids = [item[0] for item in data]
            # tbdbaz introduce here percentage
            # factor the decrement with a loop until one
            if len(node_related_uids) > 1:
                node_related_uids = node_related_uids[0:-1]
            put_test(node_related_uids, 'Node related', node_syndrome_testing)

            # test diagnostic algorithm with related nodes
            for diagnostic_algorithm in diagnostic_algorithm_results.keys():
                diagnostic_algorithm_results[diagnostic_algorithm]['node_syndrome_uids'] = node_syndrome_uids
                node_found_uids = diagnostic_algorithm(node_related_uids, node_syndrome_testing)
                put_test(node_found_uids, 'Node found', node_syndrome_testing)
                if node_syndrome_uid in node_found_uids:
                    diagnostic_algorithm_results[diagnostic_algorithm]['node_found_uids'].append(node_syndrome_uid)

        # print results
        print()
        print()
        for diagnostic_algorithm in diagnostic_algorithm_results.keys():
            print('    Diagnostic algorithm name:', diagnostic_algorithm_results[diagnostic_algorithm]['name'])
            if node_syndrome_testing:
                print('        Node syndrome uids   :', sorted(diagnostic_algorithm_results[diagnostic_algorithm]['node_syndrome_uids']))
                print('        Node found uids      :', sorted(diagnostic_algorithm_results[diagnostic_algorithm]['node_found_uids']))
            else:
                print('        Node syndrome count  :', len(diagnostic_algorithm_results[diagnostic_algorithm]['node_syndrome_uids']))
                print('        Node found count     :', len(diagnostic_algorithm_results[diagnostic_algorithm]['node_found_uids']))
            print('        Node found percent   :', 100 * len(diagnostic_algorithm_results[diagnostic_algorithm]['node_found_uids']) /
                                                          len(diagnostic_algorithm_results[diagnostic_algorithm]['node_syndrome_uids']))
            print()

        # uncomment 6 following lines to display repartition of syndromes per number of symptoms
#        plt.figure()
#        plt.axis([1, 30, 0, 40])
#        plt.xlabel('Symptoms')
#        plt.ylabel('Number of syndromes that have')
#        plt.hist(number_symptoms_per_syndrome, bins=27)
#        plt.show()

#        all_functions = inspect.getmembers(test_scenario_class, inspect.isfunction())
#        print(all_functions)


if __name__ == '__main__':
    pass
