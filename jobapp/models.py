from django.db import models

# Create your models here.
class ITJobs(models.Model):
    company_name=models.CharField(max_length=50)
    job_profile=models.CharField(max_length=50)
    job_discription=models.CharField(max_length=100)
    job_requirements=models.CharField(max_length=100)
    experience=models.FloatField()
    package=models.FloatField()
    no_of_vaccancy=models.IntegerField()
    location=models.CharField(max_length=50)
    Mod_date=models.DateField()
    last_date=models.DateField()

class MechJobs(models.Model):
    company_name=models.CharField(max_length=50)
    job_profile=models.CharField(max_length=50)
    job_discription=models.CharField(max_length=100)
    job_requirements=models.CharField(max_length=100)
    experience=models.FloatField()
    package=models.FloatField()
    no_of_vaccancy=models.IntegerField()
    location=models.CharField(max_length=50)
    Mod_date=models.DateField()
    last_date=models.DateField()

class CivilJobs(models.Model):
    company_name=models.CharField(max_length=50)
    job_profile=models.CharField(max_length=50)
    job_discription=models.CharField(max_length=100)
    job_requirements=models.CharField(max_length=100)
    experience=models.FloatField()
    package=models.FloatField()
    no_of_vaccancy=models.IntegerField()
    location=models.CharField(max_length=50)
    Mod_date=models.DateField()
    last_date=models.DateField()

class JobsApplied(models.Model):
    user_id= models.IntegerField()
    job_id= models.IntegerField()
    job_cat= models.CharField(max_length=10)

class UserData(models.Model):
    user_id = models.IntegerField()
    image = models.ImageField(upload_to='pics', blank=True, null=True)
    resume = models.FileField(upload_to='pics', blank=True, null=True)
    education = models.CharField(max_length=100)
    experience = models.CharField(max_length=100)
    phone_no = models.IntegerField(null=False, blank=False, unique=True)
