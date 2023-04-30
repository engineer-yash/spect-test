from django.shortcuts import render,HttpResponseRedirect

def index(request):
    return render(request, "web/index.html")


def showslides(request):
    return render(request, "web/index.html")

#Create a view Function for  show all events
def Events(request , event_name):
    # if event_name=="spectrom":
    #     event_data = model_name(request)
    # if event_name=="digirace":
    #     event_data = model_name(request)
    # if event_name=="golafek":
    #     event_data = model_name(request)
    # else:
    #     return HttpResponseRedirect('/')
    return render(request , 'web/Events.html' )


