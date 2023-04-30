from django.shortcuts import render

# Create your views here.

def host_index(request):
    return render(request, "event_host/event_host.html")
