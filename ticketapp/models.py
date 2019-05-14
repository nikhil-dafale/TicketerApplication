from django.db import models
from django.contrib.auth.models import User

class Ticket(models.Model):
    status_choice=(("Open",'open'),("Closed",'closed '))

    user=models.ForeignKey(User, on_delete=models.CASCADE)
    title=models.CharField(max_length=50)
    body=models.CharField(max_length=100)
    status=models.CharField(max_length=10,choices=status_choice,default="Open")
    #user info
    author=User.username
    #user
    assignee=models.CharField(max_length=100)
    #date
    created=models.DateField(auto_now=True)

    def __str__(self):
        return self.title+"-"+self.body


