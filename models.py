from django.db import models

# Create your models here.
class user(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(unique=True)
    password=models.CharField()

    def __str__(self):
        return self.name
    


class job(models.Model):
    title=models.CharField(max_length=100)
    company=models.CharField(max_length=100)
    description=models.TextField()



    def __str__(self):
        return self.titale