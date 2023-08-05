from django.db import models

from django.contrib.auth.models import User

# Create your models here.

# All the type of jobs


class JobRole(models.Model):
    category = models.CharField(max_length=180, blank=False, null=False)

    def __str__(self):
        return self.category


# For recruiter to put


class CompanyRole(models.Model):
    category = models.ForeignKey(JobRole, on_delete=models.CASCADE)
    title = models.CharField(max_length=180, null=False, blank=False)
    offered_CTC = models.IntegerField(null=False, blank=False, default=0)
    location = models.CharField(max_length=200, blank=False, null=False)

    def __str__(self):
        return self.title


# For user to choose

class UserRole(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    interested_roles = models.ManyToManyField(JobRole)
    location_pref = models.CharField(max_length=180, null=True, blank=False)
    current_CTC = models.IntegerField(null=False, blank=False, default=0)
    expected_CTC = models.IntegerField(null=False, blank=False, default=0)

    def __str__(self):
        return self.user.username
