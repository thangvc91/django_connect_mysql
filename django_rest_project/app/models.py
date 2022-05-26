from django.db import models

# Create your models here.
class Userdb(models.Model):
    name = models.CharField(max_length=100, null=True)
    email = models.CharField(max_length=100, null=True)
    phone = models.CharField(max_length=100, null=True)
    def __str__(self): return self.name
    
    class Meta:
        db_table = 'user2'