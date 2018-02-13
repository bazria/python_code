#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from django.contrib.auth.models import User
from django.test import TestCase
from patient.models import Patient
from home.models import Adresse, PersonnePhysique


class PatientTestCase(TestCase):


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
        patient_none = Patient.objects.create(
            id                     = 1,
            personne               = personne_none,
            adresseCorrespondance  = adresse_none,
            social_security_number = None,
            health_care_number     = None,
        )
        user_none.save()
        adresse_none.save()
        personne_none.save()
        patient_none.save()


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
            sexe            = '',
        )
        patient_empty = Patient.objects.create(
            id                     = 2,
            personne               = personne_empty,
            adresseCorrespondance  = adresse_empty,
            social_security_number = '',
            health_care_number     = '',
        )
        user_empty.save()
        adresse_empty.save()
        personne_empty.save()
        patient_empty.save()


        user_bourreau = User.objects.create_user(
            username   = 'username_bourreau',
            password   = 'password_bourreau',
            first_name = 'Jean',
            last_name  = 'BOURREAU',
            email      = 'nmz.bourreau@gmail.com',
        )
        adresse_bourreau = Adresse.objects.create(
            numeroVoie                = '2',
            ligne_complementaire_une  = '',
            ligne_complementaire_deux = None,
            libelleVoie               = 'rue du Colonel Combes',
            localite                  = 'Paris',
            internationalPays         = None,
            codePostal                = 75016,
        )
        personne_bourreau = PersonnePhysique.objects.create(
            user            = user_bourreau,
            prenomUsuel     = 'Jean',
            nomUsage        = 'BOURREAU',
            personel_phone  = '0123456789',
            pro_phone       = '9876543210',
            telecopie       = '6789012345',
            civilite        = 'M',
            paysResidence   = 'France',
            dateNaissance   = '1999-01-31',
            sexe            = 'M',
        )
        patient_bourreau = Patient.objects.create(
            id                     = 3,
            personne               = personne_bourreau,
            adresseCorrespondance  = adresse_bourreau,
            social_security_number = '123456789012345',
            health_care_number     = '098765432109876',
        )
        user_bourreau.save()
        adresse_bourreau.save()
        personne_bourreau.save()
        patient_bourreau.save()


    def test_fhir_patient(self):
        fhir_patient = {}
        fhir_patient[0] = None
        fhir_patient[1] = {
            'resourceType': 'Patient', 'id': 1, 'text': {'status': 'encoded from anamnese', 'div   ': 'tbd'}, 'active': 'true',
            'address': None,
            'animal': 'false',
            'birthDate': None,
            'communication': [{'language': { 'coding': [{'system': 'urn:ietf:bcp:47', 'code': 'fr', 'display': 'Français'}], 'text': 'France'}, 'preferred': 'true'}], 'contact': None,
            'deceasedBoolean': 'false', 'deceasedDateTime': None,
            'gender': 'Unknown',
            'generalPractitioner': None, 'identifier': None, 'link': None, 'managingOrganization': None,
            'maritalStatus': { 'coding': [{'system': 'http://hl7.org/fhir/v3/MaritalStatus', 'code': None, 'display': 'Unknown'}], 'text': 'Unknown'},
            'multipleBirthBoolean': None, 'multipleBirthInteger': None,
            'name': [],
            'photo': None,
            'telecom': []
        }
        fhir_patient[2] = {
            'resourceType': 'Patient', 'id': 2, 'text': {'status': 'encoded from anamnese', 'div   ': 'tbd'}, 'active': 'true',
            'address': None,
            'animal': 'false',
            'birthDate': None,
            'communication': [{'language': { 'coding': [{'system': 'urn:ietf:bcp:47', 'code': 'fr', 'display': 'Français'}], 'text': 'France'}, 'preferred': 'true'}], 'contact': None,
            'deceasedBoolean': 'false', 'deceasedDateTime': None,
            'gender': 'Unknown',
            'generalPractitioner': None, 'identifier': None, 'link': None, 'managingOrganization': None,
            'maritalStatus': { 'coding': [{'system': 'http://hl7.org/fhir/v3/MaritalStatus', 'code': None, 'display': 'Unknown'}], 'text': 'Unknown'},
            'multipleBirthBoolean': None, 'multipleBirthInteger': None,
            'name': [],
            'photo': None,
            'telecom': []
        }
        fhir_patient[3] = {

            'resourceType': 'Patient', 'id': 3, 'text': {'status': 'encoded from anamnese', 'div   ': 'tbd'},
             'active': 'true', 'address': [
                {'use': 'home', 'line': ['2 rue du Colonel Combes'], 'postalCode': '75016', 'city': 'Paris',
                 'country': 'France'}], 'animal': 'false', 'birthDate': '1999-01-31', 'communication': [{'language': {
                'coding': [{'system': 'urn:ietf:bcp:47', 'code': 'fr', 'display': 'Français'}], 'text': 'France'},
                                                                                                         'preferred': 'true'}],
             'contact': None, 'deceasedBoolean': 'false', 'deceasedDateTime': None, 'gender': 'male',
             'generalPractitioner': None, 'identifier': None, 'link': None, 'managingOrganization': None,
             'maritalStatus': {
                 'coding': [{'system': 'http://hl7.org/fhir/v3/MaritalStatus', 'code': None, 'display': 'Unknown'}],
                 'text': 'Unknown'}, 'multipleBirthBoolean': None, 'multipleBirthInteger': None,
             'name': [{'use': 'usual', 'family': 'BOURREAU', 'given': ['Jean'], 'suffix': 'M'}], 'photo': None,
             'telecom': [{'system': 'phone', 'value': '0123456789', 'use': 'home'},
                         {'system': 'phone', 'value': '9876543210', 'use': 'work'},
                         {'system': 'email', 'value': 'nmz.bourreau@gmail.com', 'use': 'home'}]
        }


#        def get_anamnese_patient(patient_id):
#            try:
#                anamnese_patient = Patient.objects.get(id = patient_id).get_personal_info()
#                return anamnese_patient
#            except Exception as exception_other:
#                print("    Exception : %s" % exception_other)
#                print("    patient_id:", patient_id)
#                return None


        for patient_id in range(1, 4):
#            anamnese_patient = get_anamnese_patient(patient_id = patient_id)
#            print('anamnese_patient:')
#            print(anamnese_patient)
#            print('fhir_patient:')
#            print(Patient.fhir_patient_json(patient_id))
            self.assertEqual(Patient.fhir_patient_json(patient_id), fhir_patient[patient_id])
