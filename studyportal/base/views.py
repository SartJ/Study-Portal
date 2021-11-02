from django.shortcuts import render
from .models import Room, Profile
# Create your views here.

# rooms = [

#     {'id':1, 'name':'Python'},
#     {'id':2, 'name':'Javascript'},
#     {'id':3, 'name':'C++'},

# ]

# profiles = [

#     {'id':1, 'username':'Sartaj'},
#     {'id':2, 'username':'Tanzim'},
#     {'id':3, 'username':'Aryan'},
#     {'id':4, 'username':'Mushaidul'},

# ]

def home(request):
    rooms = Room.objects.all()
    context = {'rooms': rooms}
    return render(request, 'base/home.html', context)

def room(request, pk):
    room = Room.objects.get(id=pk)
    context = {'room': room}
    return render(request, 'base/room.html', context)

def gallery(request):
    profiles = Profile.objects.all()
    context = {'profiles': profiles}
    return render(request, 'base/gallery.html', context)

def profile(request, pk):
    profile = Profile.objects.get(id=pk)
    context = {'profile': profile}
    return render(request, 'base/profile.html', context)