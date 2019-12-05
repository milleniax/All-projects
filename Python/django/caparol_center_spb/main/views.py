from django.shortcuts import redirect, render
from .models import Question
from django.http import HttpResponseRedirect
from django.urls import reverse

def main_render(request):
    return render(request, 'main/index.html')

def question(request):
    if request.method == 'POST':
        phone = request.POST.get("phone")
        vk = request.POST.get("vk")
        email = request.POST.get("email")
        
        Question.objects.create(phone = request.POST['phone'],
                                vk = request.POST['vk'],
                                email = request.POST['email'])
    
    return HttpResponseRedirect(reverse('main:main_render'))

