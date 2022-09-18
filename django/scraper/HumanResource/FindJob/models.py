from django.db import models

# Create your models here.

class HumanSourceEntities(models.Model):
    title = models.CharField(max_length=50)
    company = models.CharField(max_length=50)
    location = models.CharField(max_length=10)
    salary = models.CharField(max_length=30)
    createdAt = models.DateField(auto_now_add=True)

    class Meta:
        db_table = 'Search_job'
        
