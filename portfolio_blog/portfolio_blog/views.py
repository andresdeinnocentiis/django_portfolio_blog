from django.shortcuts import render



# PROJECT VIEWS:


def home(request):
    return render(request, 'index.html', {})

def contact(request):
    return render(request, 'pages/Contact/contact.html')

def about(request):
    return render(request, 'pages/About/about.html')

def resume(request):
    return render(request, 'pages/Resume/resume.html')



