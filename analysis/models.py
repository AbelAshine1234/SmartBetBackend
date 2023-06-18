from django.db import models

# Create your models here.
class AnalysisModel(models.Model):
    title=models.CharField(max_length=10000)
    content=models.CharField(max_length=999999999999999)