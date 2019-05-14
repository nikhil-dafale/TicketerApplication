from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import authenticate,login,logout
from .forms import UserForm,TicketForm,TicketFilter
from .models import Ticket

#creating the ticket
def create_ticket(request):
    if not request.user.is_authenticated():
        return render(request,'login.html')

    else:
        form=TicketForm(request.POST or None)
        if form.is_valid():
            ticket=form.save(commit=False)
            ticket.user=request.user
            ticket.save()
            return render(request,'detail.html',{'ticket':ticket})

    return render(request,'create_ticket.html')


def edit_ticket(request,ticket_id):
    ticket=get_object_or_404(Ticket,ticket_id)

    if not request.user.is_authenticated():
        return render(request,'login.html')

    else:
        form=TicketForm(request.POST or None)
        if form.is_valid():
            ticket=form.save(commit=False)
            ticket.user=request.user
            ticket.save()
            return render(request,'detail.html',{'ticket':ticket})

    return render(request,'index.html',{'form':form, 'ticket':ticket.title})


def delete_ticket(request,ticket_id):
    ticket=Ticket.objects.get(pk=ticket_id)
    ticket.delete()

    tickets=Ticket.objects.filter(user=request.user)
    return render(request,'index.html',{'tickets':ticket})


def logout_user(request):
    logout(request)
    form=UserForm(request.POST or None)
    context={'form':form}
    return render(request,'login.html',context)


def login_user(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(username=username,password=password)

        if user is not None:
            if user.is_active:
                login(request,user)
                tickets=Ticket.objects.filter(user=request.user)
                return render(request,'index.html',{'tickets':tickets})
            else:
                return render(request,'index.html',{'error_message':"Your account is disabled"})

        else:
            return render(request,'login.html',{'error_message':'Invalid Login Credentials'})

    return render(request,'login.html')



def details(request,ticket_id):
    if not request.user.is_authenticated():
        return render(request,'login.html')
    else:
        user=request.user
        ticket=get_object_or_404(Ticket,pk=ticket_id)
        return render(request,'detail.html',{'ticket':ticket, 'user':user})


def register(request):
    form=UserForm(request.POST or None)

    if form.is_valid():
        user=form.save(commit=False)
        username=form.cleaned_data['username']
        password=form.cleaned_data['password']
        user.set_password(password)

        if user is not None:
            if user.is_active:
                login(request,user)
                tickets=Ticket.objects.filter(user=request.user)
                return render(request,'index.html',{'tickets':tickets})

    return render(request,'register.html',{'form':form})


def index(request):
    if not request.user.is_authenticated:
        return render(request,'login.html')
    else:
        tickets=Ticket.objects.filter(user=request.user)
        '''query = request.GET.get("q")
               if query:
                   tickets = tickets.filter(Q(ticket_title__icontains=query)).distinct()
                   return render(request, 'dashboard/index.html', {'tickets': tickets,})
               else:'''
        return render(request, 'index.html', {'tickets': tickets})


def ticket_list(request):
    ticket_filter=TicketFilter(request.GET,queryset=Ticket.objects.all())
    return render(request,'index.html',{'filter':ticket_filter})