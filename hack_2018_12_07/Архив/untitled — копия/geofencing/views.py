from django.shortcuts import render


def geofencing(request):

    return render(request, 'geofencing.html', locals())