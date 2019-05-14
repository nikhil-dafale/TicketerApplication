from django.conf.urls import url
from . import views

app_name='ticketapp'

urlpatterns=[
    url(r'^index$',views.index,name='index'),
    url(r'^register/$',views.register,name='register'),
    url(r'^login_user/$',views.login_user,name='login_user'),
    url(r'^logout_user/$',views.logout_user,name='logout_user'),
    url(r'^(?P<ticket_id>[0-9]+)/$',views.details,name='details'),
    url(r'^create_ticket/$',views.create_ticket, name='create_ticket'),
    url(r'^(?P<ticket_id>[0-9]+)/delete_ticket/$',views.delete_ticket,name='delete_ticket'),
    url(r'^(?P<ticket_id>[0-9]+)/edit_ticket$',views.edit_ticket,name='edit_ticket')
]