from django import  forms
import django_filters
from django.contrib.auth.models import User
from .models import Ticket

class UserForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput)

    class Meta:
        models=User
        fields=['username','email','password']


class TicketForm(forms.ModelForm):
    class Meta:
        models=Ticket
        fields=['title','body','status','user']


class TicketFilter(django_filters.FilterSet):
    class Meta:
        models=Ticket
        fields=['title','status']