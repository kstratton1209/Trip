from django.db import models
from apps.login.models import Registration
import re
from time import gmtime, strftime


# Create your models here.

class TripsManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        # add keys and values to errors dictionary for each invalid field
        if len(postData['destination']) < 4:
            errors["destination"] = "A destination must consist of at least 3 characters."
        if len(postData['plan']) < 4:
            errors["plan"] = "A plan must be provided and consist of at least 3 characters!" 
        if len(postData['start_date']) < 1:
            errors["start_date"] = "A start date must be provided."    
        if len(postData['end_date']) < 1:
            errors["end_date"] = "A start date must be provided."
        if postData["start_date"] < strftime("%Y-%m-%d %H:%M %p", gmtime()):
            errors["future_start_date"] = "Start date cannot be in the past!"   
        if postData["start_date"] > postData["end_date"]:
            errors["future_end_date"] = "Start date cannot be before end date!"        
        return errors

class Trips(models.Model):
    user = models.ForeignKey(Registration, related_name = "user_trips", on_delete = models.CASCADE)
    destination = models.TextField()
    plan = models.TextField()
    join = models.ManyToManyField(Registration, related_name = "user_joins")
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = TripsManager()

