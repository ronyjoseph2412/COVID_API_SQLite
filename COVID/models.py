from django.db import models
from django.core.validators import MaxValueValidator
# Create your models here.

class COVID_India(models.Model):
    Region=models.CharField(max_length = 20,primary_key=True)
    Total_Cases=models.IntegerField(validators=[MaxValueValidator(999999999999999)])
    Positive_Cases_Today=models.IntegerField(validators=[MaxValueValidator(999999999999999)])
    Active_Cases=models.IntegerField(validators=[MaxValueValidator(999999999999999)])
    Total_Cases_Recovered=models.IntegerField(validators=[MaxValueValidator(999999999999999)])
    Daily_Cases_Recovered=models.IntegerField(validators=[MaxValueValidator(999999999999999)])
    Confirmed_Deaths=models.IntegerField(validators=[MaxValueValidator(999999999999999)])
    Deaths_Per_Day=models.IntegerField(validators=[MaxValueValidator(999999999999999)])
    Active_Cases_Ratio=models.FloatField()
    
