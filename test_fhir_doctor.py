#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from django.contrib.auth.models import User
from django.test import TestCase
from doctor.models import Cabinet, Professionnel
from home.models import Adresse, PersonnePhysique


class DoctorTestCase(TestCase):


    def setUp(self):
        user_none = User.objects.create_user(
            username   = 'username_none',
            password   = None,
            first_name = '',
            last_name  = '',
            email      = None,
        )
        adresse_none = Adresse.objects.create(
            numeroVoie                = None,
            ligne_complementaire_une  = None,
            ligne_complementaire_deux = None,
            libelleVoie               = None,
            localite                  = None,
            internationalPays         = None,
            codePostal                = None,
        )
        personne_none = PersonnePhysique.objects.create(
            user            = user_none,
            prenomUsuel     = '',
            nomUsage        = '',
            personel_phone  = None,
            pro_phone       = None,
            telecopie       = None,
            civilite        = '',
            paysResidence   = '',
            dateNaissance   = None,
            sexe            = '',
        )
        cabinet_none = Cabinet.objects.create(
            adresse   = adresse_none,
            telephone = None,
        )
        professionnel_none = Professionnel.objects.create(
            id                    = 1,
            personne              = personne_none,
            typeIdNat_PP          = '',
            idpp                  = '',
            idNat_PS              = '',
            adresseCorrespondance = adresse_none,
        )
        professionnel_none.cabinet.add(cabinet_none)
        user_none.save()
        adresse_none.save()
        personne_none.save()
        cabinet_none.save()
        professionnel_none.save()


        user_empty = User.objects.create_user(
            username   = 'username_empty',
            password   = '',
            first_name = '',
            last_name  = '',
            email      = '',
        )
        adresse_empty = Adresse.objects.create(
            numeroVoie                = '',
            ligne_complementaire_une  = '',
            ligne_complementaire_deux = '',
            libelleVoie               = '',
            localite                  = '',
            internationalPays         = '',
            codePostal                = '',
        )
        personne_empty = PersonnePhysique.objects.create(
            user            = user_empty,
            prenomUsuel     = '',
            nomUsage        = '',
            personel_phone  = '',
            pro_phone       = '',
            telecopie       = '',
            civilite        = '',
            paysResidence   = '',
            dateNaissance   = None,
            sexe            = 'F',
        )
        cabinet_empty = Cabinet.objects.create(
            adresse   = adresse_empty,
            telephone = '',
        )
        professionnel_empty = Professionnel.objects.create(
            id                    = 2,
            personne              = personne_empty,
            typeIdNat_PP          = '',
            idpp                  = '',
            idNat_PS              = '',
            adresseCorrespondance = adresse_empty,
        )
        professionnel_empty.cabinet.add(cabinet_empty)
        user_empty.save()
        adresse_empty.save()
        personne_empty.save()
        cabinet_empty.save()
        professionnel_empty.save()


        user_frankenstein = User.objects.create_user(
            username   = 'username_frankenstein',
            password   = 'password_frankenstein',
            first_name = 'Victor',
            last_name  = 'FRANKENSTEIN',
            email      = 'victor@frankenstein.doc',
        )
        adresse_frankenstein = Adresse.objects.create(
            numeroVoie                = '1',
            ligne_complementaire_une  = 'eins',
            ligne_complementaire_deux = 'Mühltal Burg',
            libelleVoie               = 'Ralphweg',
            localite                  = 'Frankenstein',
            internationalPays         = '67468',
            codePostal                = '67468',
        )
        personne_frankenstein = PersonnePhysique.objects.create(
            user            = user_frankenstein,
            prenomUsuel     = 'Victor',
            nomUsage        = 'FRANKENSTEIN',
            personel_phone  = '+49 0 1111111111',
            pro_phone       = '+49 1 1111111111',
            telecopie       = '+49 2 1111111111',
            civilite        = 'M',
            paysResidence   = 'Germany',
            dateNaissance   = '1831-01-01',
            sexe            = 'M',
        )
        cabinet_frankenstein = Cabinet.objects.create(
            adresse   = adresse_frankenstein,
            telephone = '+49 3 1111111111',
        )
        professionnel_frankenstein = Professionnel.objects.create(
            id                    = 3,
            personne              = personne_frankenstein,
            typeIdNat_PP          = '1',
            idpp                  = '111',
            idNat_PS              = '11 11 11 11 11 11 11 11',
            adresseCorrespondance = adresse_frankenstein,
        )
        professionnel_frankenstein.cabinet.add(cabinet_frankenstein)
        user_frankenstein.save()
        adresse_frankenstein.save()
        personne_frankenstein.save()
        cabinet_frankenstein.save()
        professionnel_frankenstein.save()


        user_schweitzer = User.objects.create_user(
            username   = 'username_schweitzer',
            password   = 'password_schweitzer',
            first_name = 'Albert',
            last_name  = 'SCHWEITZER',
            email      = 'albert@schweitzer.org',
        )
        adresse_schweitzer = Adresse.objects.create(
            numeroVoie                = '4',
            ligne_complementaire_une  = '',
            ligne_complementaire_deux = '',
            libelleVoie               = '',
            localite                  = 'Kaysersberg',
            internationalPays         = '444444',
            codePostal                = '444444',
        )
        personne_schweitzer = PersonnePhysique.objects.create(
            user            = user_schweitzer,
            prenomUsuel     = 'Albert',
            nomUsage        = 'SCHWEITZER',
            personel_phone  = '+49 0 4444444444',
            pro_phone       = '+49 4 4444444444',
            telecopie       = '+49 2 4444444444',
            civilite        = 'M',
            paysResidence   = 'Gabon',
            dateNaissance   = '1875-01-14',
            sexe            = 'M',
        )
        cabinet_schweitzer = Cabinet.objects.create(
            adresse   = adresse_schweitzer,
            telephone = '+49 3 4444444444',
        )
        professionnel_schweitzer = Professionnel.objects.create(
            id                    = 4,
            personne              = personne_schweitzer,
            typeIdNat_PP          = '4',
            idpp                  = '444',
            idNat_PS              = '44 44 44 44 44 44 44 44',
            adresseCorrespondance = adresse_schweitzer,
        )
        professionnel_schweitzer.cabinet.add(cabinet_schweitzer)
        user_schweitzer.save()
        adresse_schweitzer.save()
        personne_schweitzer.save()
        cabinet_schweitzer.save()
        professionnel_schweitzer.save()


        user_house = User.objects.create_user(
            username   = 'username_house',
            password   = 'password_house',
            first_name = 'Gregory',
            last_name  = 'HOUSE',
            email      = 'gregory@house.com',
        )
        adresse_house = Adresse.objects.create(
            numeroVoie                = '221',
            ligne_complementaire_une  = 'B',
            ligne_complementaire_deux = 'NJ',
            libelleVoie               = 'Baket Street',
            localite                  = 'Princeton',
            internationalPays         = '555555',
            codePostal                = '555555',
        )
        personne_house = PersonnePhysique.objects.create(
            user            = user_house,
            prenomUsuel     = 'Gregory',
            nomUsage        = 'HOUSE',
            personel_phone  = '+59 0 5555555555',
            pro_phone       = '+59 5 5555555555',
            telecopie       = '+59 2 5555555555',
            civilite        = 'M',
            paysResidence   = 'United States of America',
            dateNaissance   = '1959-06-11',
            sexe            = 'M',
        )
        cabinet_house = Cabinet.objects.create(
            adresse   = adresse_house,
            telephone = '+59 3 5555555555',
        )
        professionnel_house = Professionnel.objects.create(
            id                    = 5,
            personne              = personne_house,
            typeIdNat_PP          = '5',
            idpp                  = '555',
            idNat_PS              = '55 55 55 55 55 55 55 55',
            adresseCorrespondance = adresse_house,
        )
        professionnel_house.cabinet.add(cabinet_house)
        user_house.save()
        adresse_house.save()
        personne_house.save()
        cabinet_house.save()
        professionnel_house.save()


    def test_fhir_doctor(self):
        fhir_doctor = {}
        fhir_doctor[0] = None
        fhir_doctor[1] = {
            'resourceType': 'Practitioner', 'id': 1, 'text': {'status': 'encoded from anamnese', 'div': 'tbd'}, 'active': 'true',
            'address': [],
            'birthDate': None,
            'communication': [{'language': { 'coding': [{'system': 'urn:ietf:bcp:47', 'code': 'fr', 'display': 'Français'}], 'text': 'France'}, 'preferred': 'true'}],
            'gender': 'Unknown',
            'identifier': None,
            'name': [],
            'photo': None,
            'telecom': []
        }
        fhir_doctor[2] = {
            'resourceType': 'Practitioner', 'id': 2, 'text': {'status': 'encoded from anamnese', 'div': 'tbd'}, 'active': 'true',
            'address': [],
            'birthDate': None,
            'communication': [{'language': { 'coding': [{'system': 'urn:ietf:bcp:47', 'code': 'fr', 'display': 'Français'}], 'text': 'France'}, 'preferred': 'true'}],
            'gender': 'female',
            'identifier': None,
            'name': [],
            'photo': None,
            'telecom': []
        }
        fhir_doctor[3] = {
            'resourceType': 'Practitioner', 'id': 3, 'text': {'status': 'encoded from anamnese', 'div': 'tbd'}, 'active': 'true',
            'address': [ {'use': 'work', 'line': ['1 Ralphweg'], 'postalCode': '67468', 'city': 'Frankenstein', 'country': 'Germany'}],
            'birthDate': '1831-01-01',
            'communication': [{'language': { 'coding': [{'system': 'urn:ietf:bcp:47', 'code': 'fr', 'display': 'Français'}], 'text': 'France'}, 'preferred': 'true'}],
            'gender': 'male',
            'identifier': '11 11 11 11 11 11 11 11',
            'name': [{'use': 'usual', 'family': 'FRANKENSTEIN', 'given': ['Victor'], 'suffix': 'M'}],
            'photo': None,
            'telecom': [{'system': 'phone', 'value': '+49 0 1111111111', 'use': 'home'},
                        {'system': 'phone', 'value': '+49 1 1111111111', 'use': 'work'},
                        {'system': 'email', 'value': 'victor@frankenstein.doc', 'use': 'work'},
                        {'system': 'fax', 'value': '+49 2 1111111111', 'use': 'work'}]
        }
        fhir_doctor[4] = {
            'resourceType': 'Practitioner', 'id': 4, 'text': {'status': 'encoded from anamnese', 'div': 'tbd'}, 'active': 'true',
            'address': [ {'use': 'work', 'line': ['4 '], 'postalCode': '444444', 'city': 'Kaysersberg', 'country': 'Gabon'}],
            'birthDate': '1875-01-14',
            'communication': [{'language': { 'coding': [{'system': 'urn:ietf:bcp:47', 'code': 'fr', 'display': 'Français'}], 'text': 'France'}, 'preferred': 'true'}],
            'gender': 'male',
            'identifier': '44 44 44 44 44 44 44 44',
            'name': [{'use': 'usual', 'family': 'SCHWEITZER', 'given': ['Albert'], 'suffix': 'M'}],
            'photo': None,
            'telecom': [{'system': 'phone', 'value': '+49 0 4444444444', 'use': 'home'},
                        {'system': 'phone', 'value': '+49 4 4444444444', 'use': 'work'},
                        {'system': 'email', 'value': 'albert@schweitzer.org', 'use': 'work'},
                        {'system': 'fax', 'value': '+49 2 4444444444', 'use': 'work'}]
        }
        fhir_doctor[5] = {
            'resourceType': 'Practitioner', 'id': 5, 'text': {'status': 'encoded from anamnese', 'div': 'tbd'}, 'active': 'true',
            'address': [ {'use': 'work', 'line': ['221 Baket Street'], 'postalCode': '555555', 'city': 'Princeton', 'country': 'United States of America'}],
            'birthDate': '1959-06-11',
            'communication': [{'language': { 'coding': [{'system': 'urn:ietf:bcp:47', 'code': 'fr', 'display': 'Français'}], 'text': 'France'}, 'preferred': 'true'}],
            'gender': 'male',
            'identifier': '55 55 55 55 55 55 55 55',
            'name': [{'use': 'usual', 'family': 'HOUSE', 'given': ['Gregory'], 'suffix': 'M'}],
            'photo': None,
            'telecom': [{'system': 'phone', 'value': '+59 0 5555555555', 'use': 'home'},
                        {'system': 'phone', 'value': '+59 5 5555555555', 'use': 'work'},
                        {'system': 'email', 'value': 'gregory@house.com', 'use': 'work'},
                        {'system': 'fax', 'value': '+59 2 5555555555', 'use': 'work'}]
        }


#        def get_anamnese_practitioner(practitioner_id):
#            try:
#                anamnese_practitioner = Professionnel.objects.get(id=practitioner_id).get_personal_info()
#                return anamnese_practitioner
#            except Exception as exception_other:
#                print("    Exception : %s" % exception_other)
#                print("    practitioner_id:", practitioner_id)
#                return None


        for practitioner_id in range(1, 6):
#            anamnese_practitioner = get_anamnese_practitioner(practitioner_id = practitioner_id)
#            print('anamnese_practitioner:')
#            print(anamnese_practitioner)
#            print('fhir_practitioner:')
#            print(Professionnel.fhir_practitioner_json(practitioner_id))
            self.assertEqual(Professionnel.fhir_practitioner_json(practitioner_id), fhir_doctor[practitioner_id])
