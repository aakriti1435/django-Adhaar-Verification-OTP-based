from django.db import models

# Create your models here.
class DummyAadharData(models.Model):
    person_id = models.AutoField(primary_key=True)
    firt_name = models.CharField(max_length=100, null=True, blank=True, default="")
    last_name = models.CharField(max_length=100, null=True, blank=True, default="")
    date_of_birth = models.DateField(auto_now=False)
    sex = models.CharField(max_length=10, null=True, blank=True, default="")
    address = models.CharField(max_length=500, null=True, blank=True, default="")
    mobile = models.BigIntegerField(default=0, null=True, blank=True)
    aadhar_no = models.CharField(max_length=12, null=True, blank=True, default="", unique=True)
    email_id = models.EmailField(default="", blank=True, null=True)


    def __str__(self):
        return self.firt_name
