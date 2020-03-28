from django.shortcuts import redirect, render
from .forms import EmailForm
from django.views.generic.edit import FormView
from django.core.mail import send_mail
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse
from .models import Subscriber


class ContactView(SuccessMessageMixin, FormView):
    template_name = 'main/index.html'
    form_class = EmailForm
    success_url = 'main/index.html'
    success_message = "Письмо успешно отправлено"

    def form_valid(self, form):
        email = form.cleaned_data['email']
        send_mail('Caparol_Center_Spb',
                  'Теперь вы будете получать лучшие предложения шоу-рума',
                  email,
                  [email, ],
                  fail_silently=False,)
        success_message = self.get_success_message(form.cleaned_data)
        if success_message:
            messages.success(self.request, success_message)

        if not Subscriber.objects.filter(email=email).exists():
            Subscriber.objects.create(email=email)
        return redirect(reverse('main:index'))

    def form_invalid(self, form):
        return HttpResponse('Unsuccess')
