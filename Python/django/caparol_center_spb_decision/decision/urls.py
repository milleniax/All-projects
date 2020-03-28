from django.urls import path
from .views import ContactView

app_name = 'decision'

urlpatterns = [
    path('livingrooms/', ContactView.as_view(), name='livingrooms')
]
