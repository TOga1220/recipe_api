from django.db import models

# Create your models here.
class Recipe(models.Model):
    title = models.CharField(max_length=100)
    making_time = models.CharField(max_length=100)
    serves = models.CharField(max_length=100)
    ingredients = models.CharField(max_length=300)
    cost = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'recipes'   
