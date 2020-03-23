from django.shortcuts import render
from django.contrib import messages

# Create your views here.
def index(request):
    context = {'home' : True}
    messages.success(request, 'Hello')
    return render(request, 'index.html', context)