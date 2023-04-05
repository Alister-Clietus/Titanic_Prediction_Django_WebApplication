from django.db import models

# Create your models here.
class Data(models.Model):
    name = models.CharField(max_length=100, null=True)
    PClass = models.PositiveIntegerField(null=True)
    Sex = models.PositiveIntegerField(null=True)
    Age = models.PositiveIntegerField(null=True)
    Sibsp = models.PositiveIntegerField(null=True)
    Parch = models.PositiveIntegerField(null=True)
    Fare = models.PositiveIntegerField(null=True)
    Embarked = models.PositiveIntegerField(null=True)
    predictions = models.PositiveIntegerField(null=True)
    date = models.DateTimeField(auto_now_add=True)

class Meta:
    ordering = ['-date']    

def _str_(self):
    return self.name