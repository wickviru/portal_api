from django.db import models
from company import models as company
from candidate import models as candidate
# Create your models here.

class job(models.Model):
    owner = models.ForeignKey(company.Auth,on_delete=models.CASCADE)
    eligibility = models.CharField(max_length=200)
    requirements = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    profile = models.CharField(max_length=200)
    ctc = models.CharField(max_length=200)
    lastdateapply = models.DateField(max_length=200)

class applied(models.Model):
    jobid = models.ForeignKey(job,on_delete=models.CASCADE)
    userid = models.ForeignKey(candidate.Auth,on_delete=models.CASCADE)
    
    