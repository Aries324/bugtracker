from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.timezone import now
from model_utils import Choices

# Create your models here.
"""
Title
Time / Date filed
Description
Name of user who filed ticket
Status of ticket (New / In Progress / Done / Invalid) --> hint: https://docs.djangoproject.com/en/3.0/ref/models/fields/#choices (Links to an external site.)Links to an external site.
Name of user assigned to ticket
Name of user who completed the ticket
"""



# Create your models here.
class MyUser(AbstractUser):
    users_name = models.CharField(max_length=100, null=True, blank=True)




https://django-model-utils.readthedocs.io/en/latest/utilities.html#choices
class Ticket(models.Model):
    STATUS = Choices('New','In Progress', 'Done', 'Invalid')
    title = models.CharField(max_length=100)
    time = models.DateTimeField(default=now)
    description = models.TextField()
    user_name = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    ticket_status = models.CharField(choices=STATUS, default=STATUS.new, max_length=20)
    assigned_user =
    completed_by =

    def __str__(self):
        return self.title
