from django.http import HttpResponse

def home(request):
    print("Home page is called")
    return HttpResponse("<h1>Welcome to Django Fundamentals Learning</h1>")
