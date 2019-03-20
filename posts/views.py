from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
   # return HttpResponse('HELLO la bas')
    return render(request, 'posts/index.html')