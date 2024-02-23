from django.shortcuts import render

# Create your views here.
def base(request):
    return render(request, "authentication/login.html")

def register(request):
    return render(request, "authentication/register.html")