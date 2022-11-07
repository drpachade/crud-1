from django.db import models
# from django.utils import timezone
# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length =10)
    address = models.CharField(max_length = 30)
    phon_NO = models.CharField(max_length= 10)
    create_at = models.DateTimeField(auto_now_add = True)
    update_at = models.DateTimeField(auto_now = True)
    email_add = models.EmailField()

    def __str__(self):
        return self.name



