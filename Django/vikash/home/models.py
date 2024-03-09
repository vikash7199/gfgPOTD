from django.db import models

class student(models.Model):
    category=models.TextField();
    pname=models.CharField(max_length=100)
    sku=models.IntegerField();
    quantity=models.IntegerField()
    



