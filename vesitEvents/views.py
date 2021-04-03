from django.shortcuts import render
from .models import Events
from django.contrib import admin
from django.contrib.auth import logout
from time import strftime
import datetime
from datetime import timezone,datetime

# Create your views here.
def index(request):
    return render(request,"account/login.html")


def home(request):
    if request.user.is_authenticated:
        if request.user.groups.filter(name = "Approvers").exists():
            organizer=[]
            status=[]
            event_object=Events.objects.order_by('event_datetime')
            for event in event_object:
                x=datetime.today()
                value=event.event_datetime
                value_date_=int(value.strftime("%Y")+value.strftime("%m")+value.strftime("%d"))
                date_=int(x.strftime("%Y")+x.strftime("%m")+x.strftime("%d")) 
                if value_date_<date_:
                    print("del event")
                    Events.objects.get(event_name=event.event_name).delete()  
                else:
                    print("inside else")
                    if str(event.event_organizer) not in organizer and event.event_status==True:
                        organizer.append(str(event.event_organizer))
                    if event.event_status==True:
                        status.append(str(event.event_status))
            return render(request,"events/staff.html",{'EVENT':event_object, 'organizer':organizer, 'status':len(status) } )
        else:
            name=[]
            datetime1=[]
            duration=[]
            organizer=[]
            details=[]
            description=[]
            gformlink=[]
            status=[]
            event_object=Events.objects.order_by('event_datetime')
            # reporter = Reporters.objects.get(name='Tintin')
            print(type(event_object))
            print(event_object)
            for event in event_object:
                print(event.event_datetime)
                x=datetime.today()
                value=event.event_datetime
                value_date_=int(value.strftime("%Y")+value.strftime("%m")+value.strftime("%d"))
                date_=int(x.strftime("%Y")+x.strftime("%m")+x.strftime("%d")) 
                # print(value_date_, date_)
                if value_date_<date_:
                    print("del event")
                    Events.objects.get(event_name=event.event_name).delete()
                    continue
                name.append(str(event.event_name))
                datetime1.append(str(event.event_datetime))
                duration.append(str(event.event_duration))
                if str(event.event_organizer) not in organizer and event.event_status==True:
                    organizer.append(str(event.event_organizer))
                # details.append(str(event.event_datetime))
                description.append(str(event.event_description))
                gformlink.append(str(event.event_gformlink))
                if event.event_status==True:
                    status.append(str(event.event_status))
            
            return render(request,"events/index.html",{'EVENT':event_object, 'name':name, 'datetime':datetime1, 'duration':duration, 'organizer':organizer, 'description':description, 'gformlink':gformlink, 'status':len(status)})
    # return render(request,"account/login_check.html")


def update_status(request,eve_name,action):
    print("in unpdate")
    if request.method == "GET":
        if action==0:
            tmp = Events.objects.get(event_name=eve_name)
            tmp.event_status = True  # change field
            tmp.save()
        if action==1:
            Events.objects.get(event_name=eve_name).delete()
    organizer=[]
    status=[]
    event_object=Events.objects.order_by('event_datetime')
    for event in event_object:
        if str(event.event_organizer) not in organizer and event.event_status==True:
            organizer.append(str(event.event_organizer))
        if event.event_status==True:
            status.append(str(event.event_status))
    return render(request,"events/staff.html",{'EVENT':event_object, 'organizer':organizer, 'status':len(status) } )


def logout_view(request):
    logout(request)
    return render(request,"account/login.html")
# Redirect to a success page.


# def getRejectedBitch(request,event_name):
#     if request.method == "GET":
#         print("ggg")
#         # send mail to user whose got rejected??
#         Events.objects.get(event_name=event_name).delete()
#     organizer=[]
#     status=[]
#     event_object=Events.objects.order_by('event_datetime')
#     for event in event_object:
#         if str(event.event_organizer) not in organizer and event.event_status==True:
#             organizer.append(str(event.event_organizer))
#         if event.event_status==True:
#             status.append(str(event.event_status))
#     return render(request,"events/staff.html",{'EVENT':event_object, 'organizer':organizer, 'status':len(status) } )