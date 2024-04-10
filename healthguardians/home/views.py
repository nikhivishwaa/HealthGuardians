from django.shortcuts import render, HttpResponse

def index(request):
    return render(request, 'index.html')

# def home(request):
#     # return render(request, 'base.html')
#     return HttpResponse("hr")
