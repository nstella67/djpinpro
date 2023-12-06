from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from accountapp.models import HelloWorld


# Create your views here.

def hello_world(request):
    # return HttpResponse('Hello world!')
    if request.method == "POST":

        temp = request.POST.get('hello_world_input')

        new_hello_world = HelloWorld()
        new_hello_world.text = temp
        new_hello_world.save()

        hello_world_list = HelloWorld.objects.all()
        # return render(request, 'accountapp/hello_world.html', context={'hello_world_output': new_hello_world})
        # return render(request, 'accountapp/hello_world.html', context={'hello_world_list': hello_world_list}) -> 새로고침하면 계속 저장됨

        # accountapp 내부에 있는 hello_wordl로 재접속하라. 새로고침해도 저장되지 않는다.
        return HttpResponseRedirect(reverse('accountapp:hello_world'))
    else:
        hello_world_list = HelloWorld.objects.all()
        # return render(request, 'accountapp/hello_world.html', context={'text': 'GET METHOD!!!'})
        return render(request, 'accountapp/hello_world.html', context={'hello_world_list': hello_world_list})