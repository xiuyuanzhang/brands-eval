# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Assessment(models.Model):
    abstract = models.TextField(blank=True, null=True)
    detail = models.TextField(blank=True, null=True)
    company_name = models.TextField(blank=True, null=True)
    aspect = models.TextField(blank=True, null=True)
    post_nega = models.TextField(blank=True, null=True)
    company_id = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'assessment'


class CompanyToBrand(models.Model):
    brand_id = models.TextField(blank=True, null=True)
    brand_name = models.TextField(blank=True, null=True)
    company_name = models.TextField(blank=True, null=True)
    company_id = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'company_to_brand'


class Evaluation(models.Model):
    brand_name = models.TextField(blank=True, null=True)
    evaluation = models.TextField(blank=True, null=True)
    brand_id = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'evaluation'


class LabourRating(models.Model):
    brand_name = models.TextField(blank=True, null=True)
    labour_rating = models.TextField(blank=True, null=True)
    brand_id = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'labour_rating'


class Rating(models.Model):
    company_id = models.TextField(blank=True, null=True)
    company_name = models.TextField(blank=False, null=False)
    rating = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rating'

    def __str__(self):
        return self.company_name + "_" + self.company_id


class TransIndex(models.Model):
    brand = models.TextField(blank=True, null=True)
    policy = models.TextField(blank=True, null=True)
    tracking = models.TextField(blank=True, null=True)
    social = models.TextField(blank=True, null=True)
    engage = models.TextField(blank=True, null=True)
    governance = models.TextField(blank=True, null=True)
    score = models.TextField(blank=True, null=True)
    brand_id = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'trans_index'
