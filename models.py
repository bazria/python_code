# -*- coding: utf-8 -*-
from neomodel import (ArrayProperty, BooleanProperty, DateProperty, DateTimeProperty, FloatProperty, IntegerProperty, RelationshipFrom, RelationshipTo, StringProperty, StructuredNode, StructuredRel,
    UniqueIdProperty, AliasProperty)

from django.contrib.auth.models import User
from django.db import models
from anamnese.settings import BASE_DIR
from django.core.files import File
import os
from knowledge_database.global_variables import *
from knowledge_database.general_functions import get_updated_at, create_universal_id

class DoctorDev(models.Model):
    user = models.OneToOneField(User,related_name='doctordev')
    index_start = models.IntegerField()
    current_index = models.IntegerField()
    index_end = models.IntegerField()
    #log = models.FileField(upload_to='extra_file/log/')#, default='log/log.txt')
    log = models.CharField(max_length=300)

    def create_doctor_dev(self,username,password,index_start,index_end):
        user = User.objects.create_user(username=username,password=password)
        f = open(BASE_DIR+'/extra_file/log/'+username+'log.txt', 'w')
        path_file = str(File(f))
        dd = DoctorDev.objects.create(user=user,index_end=index_end,index_start=index_start,current_index=index_start, log='/extra_file/log/'+username+'log.txt')

class AsksAbout(StructuredRel):
    tag = StringProperty(default='discrimination')
    uid = StringProperty(default=create_universal_id())

class Causes(StructuredRel):
    tag = StringProperty()
    weight = FloatProperty()
    uid = StringProperty(default=create_universal_id())

class Chained(StructuredRel):
    uid = StringProperty(default=create_universal_id())

class Consequence(StructuredRel):
    status = StringProperty()
    uid = StringProperty(default=create_universal_id())

class IsAnswer(StructuredRel):
    weight = FloatProperty()
    uid = StringProperty(default=create_universal_id())

class IsPartOfCluster(StructuredRel):
    tag = StringProperty()
    weight = FloatProperty()
    uid = StringProperty(default=create_universal_id())

class HasExpression(StructuredRel):
    tag = StringProperty()
    weight = FloatProperty()
    uid = StringProperty(default=create_universal_id())

class IsCausedBy(StructuredRel):
    tag = StringProperty()
    weight = FloatProperty()
    uid = StringProperty(default=create_universal_id())    

class PrecisedBy(StructuredRel):
    uid = StringProperty(default=create_universal_id())
    weight = FloatProperty()
    tag = StringProperty(default ='location')

class Precision(StructuredRel):
    tag = StringProperty()
    weight = FloatProperty()
    uid = StringProperty(default=create_universal_id())



class AnamneseNode(StructuredNode):
    """
    Abstract class for all nodes in Anamnese.
    """
    __abstract_node__ = True
    uid = UniqueIdProperty()                    # baztbd unicity for node and relationship
    name = StringProperty(required=True,index=True)
    name_fr = AliasProperty(to=name)
    name_en = StringProperty()
    name_es = StringProperty()
    updated_at = IntegerProperty(default = get_updated_at())
    updated_by = StringProperty(required=True)

class DoctorNode(AnamneseNode):
    """
    Abstract class for nodes defined by doctors.
    """
    __abstract_node__ = True
    description = StringProperty()
    medical_classification = ArrayProperty(StringProperty(choices = medical_classification))
    chirurgical_classification = ArrayProperty(StringProperty(choices = chirurgical_classification))



class Indication(DoctorNode):
    """
    Class for indication nodes.
    """
    __abstract_node__ = True
    tag = StringProperty(choices = indication_tags, default='symptom')
    dangerosity = IntegerProperty(default = '0')
    synonyme = StringProperty(default='')
    #asks_about = RelationshipTo('Question', 'asks_about', model=AsksAbout)
    consequence = RelationshipFrom('Answer', 'consequence', model=Consequence)
    is_precision_of = RelationshipTo('Precision', 'precision', model=Precision)
    #is_part_of_cluster = RelationshipTo('Cluster','is_part_of_cluster',model=IsPartOfCluster)
    precised_by = RelationshipTo('Indication', 'precised_by', model=PrecisedBy)
    precises = RelationshipFrom('Indication', 'precision', model=PrecisedBy)
    #is_caused_by = RelationshipFrom('Cluster','is_caused_by',model=IsCausedBy)
    #has_expression = RelationshipFrom('Cluster', 'has_expression', model=HasExpression)

class RiskFactor(Indication):
    is_caused_by_rf = RelationshipFrom('Cluster','is_caused_by',model=IsCausedBy)
    asks_about_rf = RelationshipTo('Question', 'asks_about', model=AsksAbout)

class MedicalHistory(Indication):
    is_caused_by_mh = RelationshipFrom('Cluster','is_caused_by',model=IsCausedBy)
    asks_about_mh = RelationshipTo('Question', 'asks_about', model=AsksAbout)

class Symptom(Indication):
    has_expression = RelationshipFrom('Cluster', 'has_expression', model = HasExpression)
    asks_about_sym = RelationshipTo('Question', 'asks_about', model=AsksAbout)


class Cluster(DoctorNode):
    """
    Class for cluster nodes.
    """
    icd10_id = StringProperty()
    protocol = StringProperty(default = 'https://www.has-sante.fr/portail/')
    tag = StringProperty(choices = cluster_tags, default='syndrome')
    dangerosity = IntegerProperty(default = 0)
    is_part_of_cluster = RelationshipFrom('Cluster','is_part_of_cluster',model=IsPartOfCluster)
    is_in_drc = BooleanProperty(default = False)
    precised_by = RelationshipTo('Cluster', 'precised_by', model=PrecisedBy)
    precises = RelationshipFrom('Cluster', 'precision', model=PrecisedBy)
    causes = RelationshipTo('Cluster', 'causes', model = Causes)
    has_expression = RelationshipTo('Symptom', 'has_expression', model=HasExpression)
    is_caused_by_rf = RelationshipTo('RiskFactor','is_caused_by',model=IsCausedBy)
    is_caused_by_mh = RelationshipTo('MedicalHistory','is_caused_by',model=IsCausedBy)
    has_expression_cf = RelationshipFrom('Cluster', 'has_expression', model=HasExpression)
    is_caused_by_cf = RelationshipFrom('Cluster','is_caused_by',model=IsCausedBy)

class Question(DoctorNode):
    """
    Class for question nodes.
    """
    of_type = StringProperty(choices = question_choices, default='unique_choices')
    asks_about_rf = RelationshipFrom('RiskFactor', 'asks_about', model=AsksAbout)
    asks_about_mh = RelationshipFrom('MedicalHistory', 'asks_about', model=AsksAbout)
    asks_about_sym = RelationshipFrom('Symptom', 'asks_about', model=AsksAbout)
    is_chained_to = RelationshipFrom('Answer', 'chained', model=Chained)
    has_answer = RelationshipFrom('Answer', 'is_answer', model=IsAnswer)

class Answer(AnamneseNode):
    """
    Class for answer nodes.
    """
    consequence = StringProperty(default='')
    is_chained_to = RelationshipTo('Question', 'chained', model=Chained)
    consequence_rel = RelationshipTo('Indication', 'consequence', model=Consequence)
    is_answer_to = RelationshipTo('Question', 'is_answer', model=IsAnswer)

class Precision(AnamneseNode):
    """
    Class for precision nodes.
    """
    tag = StringProperty(required=True)
    is_precision_of = RelationshipFrom('Indication', 'precision', model=Precision)
    precised_by = RelationshipTo('Precision','precised_by',model=PrecisedBy)
    precises = RelationshipFrom('Precision','precision',model=PrecisedBy)

class Medicine(AnamneseNode):
    CIS_code = IntegerProperty()
    commercial_name = StringProperty()
    pharmaceutical_form = StringProperty()
    routes = StringProperty()
    amm_status = StringProperty()
    amm_procedure_type = StringProperty()
    marketing_status = StringProperty()
    amm_date = DateProperty()
    bdm_status = StringProperty()
    european_authorization_number = StringProperty()
    holders = StringProperty()
    reinforced_surveillance = StringProperty()
    alternative_name = StringProperty()
