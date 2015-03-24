from django.db import models

# Create your models here.

class AWSAccount(models.Model):
    account_id = models.CharField(max_length=250)

    def __unicode__(self):
        return self.account_id

class Alarm(models.Model):
    alarm_name = models.CharField(max_length=250)
    alarm_arn = models.CharField(max_length=250)

    def __unicode__(self):
        return self.alarm_name
