from django.db import models

class Boss(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=60, default='Mean Boss')
    health = models.IntegerField(default=100)
