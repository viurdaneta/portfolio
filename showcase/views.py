from django.shortcuts import render
# Create your views here.
def index(request):
    return render(request, 'showcase/index.html')

def contact(request):
    return render(request, 'showcase/contact.html')