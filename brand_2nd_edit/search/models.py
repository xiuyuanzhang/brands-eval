from django.db import models

# Create your models here.
class Rating(models.Model):
    company_id = models.TextField(blank=True, null=True)
    company_name = models.TextField(blank=True, null=True)
    rating = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'rating'

  


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
        db_table = 'trans_index'


class LabourRating(models.Model):
    brand_name = models.TextField(blank=True, null=True)
    labour_rating = models.TextField(blank=True, null=True)
    brand_id = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'labour_rating'




class Evaluation(models.Model):
    brand_name = models.TextField(blank=True, null=True)
    evaluation = models.TextField(blank=True, null=True)
    brand_id = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'evaluation'



class CompanyToBrand(models.Model):
    brand_id = models.TextField(blank=True, null=True)
    brand_name = models.TextField(blank=True, null=True)
    company_name = models.TextField(blank=True, null=True)
    company_id = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'company_to_brand'


   


class Assessment(models.Model):
    abstract = models.TextField(blank=True, null=True)
    detail = models.TextField(blank=True, null=True)
    company_name = models.TextField(blank=True, null=True)
    aspect = models.TextField(blank=True, null=True)
    post_nega = models.TextField(blank=True, null=True)
    company_id = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'assessment'






