from django.shortcuts import render, redirect
from .models import Study, Technology
from .forms import AddStudyForm, AddTechnologyForm

# Create your views here.
def get_all_studies(request):
    
    studies = Study.objects.all()
    
    context = {
        'studies': studies,   
    }
    
    return render(request, 'pages/Extra/all_studies.html', context)


def get_all_technologies(request):
    
    technologies = Technology.objects.all()
    
    context = {
        'technologies': technologies,   
    }
    
    return render(request, 'pages/Extra/all_technologies.html', context)


def add_study(request):
    if request.method == 'POST':
        
        add_study_form = AddStudyForm(request.POST, request.FILES)
        
        if add_study_form.is_valid():
            
            info = add_study_form.cleaned_data
            
            study = Study.objects.create(
                name = info['name'],
                type = info['type'],
                institution = info['institution'],
                image = info['image'],
                description = info['description'],
                from_date = info['from_date'],
                to_date = info['to_date'],
                institution_link = info['institution_link'],
                certificate_link = info['certificate_link'],
            )
            
            study.save()
            
            return redirect('/extras/studies')
        
    else:
        add_study_form = AddStudyForm()
        
    return render(request, 'pages/Extra/add_study.html', {'add_study_form': add_study_form})


def add_technology(request):
    if request.method == 'POST':
        
        add_tech_form = AddTechnologyForm(request.POST, request.FILES)
        
        if add_tech_form.is_valid():
            
            info = add_tech_form.cleaned_data
            
            tech = Technology.objects.create(
                name = info['name'],
                image = info['image'],
                years_exp = info['years_exp'],
            )
            
            tech.save()
            
            return redirect('/extras/technologies')
        
    else:
        add_tech_form = AddTechnologyForm()
        
    return render(request, 'pages/Extra/add_tech.html', {'add_tech_form': add_tech_form})