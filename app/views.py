from django.shortcuts import render
from app.models import *
from django.http import HttpResponse
# Create your views here.
def createuser(request):
    if request.method=='POST':
        em=request.POST['em']
        fn=request.POST['fn']
        ln=request.POST['ln']
        pw=request.POST['pw']
        NUO=UserProfile.objects.get_or_create(email=em,first_name=fn,last_name=ln,password=pw)[0]
        NUO.save()
        return HttpResponse('normal user is created')
    return render(request,'createuser.html')