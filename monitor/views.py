from django.shortcuts import render
from boto.ec2 import cloudwatch
from awsmonitor import settings
from monitor.models import Alarm

# Create your views here.
def update_alarms():
    conn = CloudWatchConnection(aws_access_key_id=settings.AWS_ACCESS_KEY, aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY)
    for cwa in conn.describe_alarms():
        alarm = Alarm()
        alarm.name = cwa.name
        alarm.alarm_arn = cwa.alarm_arn
        alarm.save()



update_alarms()
import ipdb; ipdb.set_trace()
