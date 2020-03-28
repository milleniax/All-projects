from django.shortcuts import render
from .forms import EmailForm
from django.views.generic.edit import FormView


class ContactView(FormView):
    template_name = 'decision/residentialInteriors.html'
    form_class = EmailForm
    success_url = 'decision/residentialInteriors.html'

    def form_valid(self, form):
        print("success")
