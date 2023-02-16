from django.shortcuts import render, redirect
from django.http import Http404
from .models import Study, Technology, Validation
from .forms import AddStudyForm, AddTechnologyForm

# Django REST Framework imports:
from .serializers import StudySerializer, TechnologySerializer, ValidationSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    CreateAPIView,
    UpdateAPIView,
    DestroyAPIView
)

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


#NOTE: STUDY VIEWS:
class GetStudyAPIView(ListAPIView):
    __doc__ = f'''
    `[GET]`
    This API view returns all the studies.
    '''
    queryset = Study.objects.all()
    serializer_class = StudySerializer
    permission_classes = [IsAuthenticated, IsAdminUser]
    
class GetSingleStudyAPIView(RetrieveAPIView):
    __doc__ = f'''
    `[GET]`
    This API view returns a single study.
    '''
    serializer_class = StudySerializer
    permission_classes = [IsAuthenticated, IsAdminUser]

    def get_object(self):
        try:
            pk = self.kwargs['pk']
            obj = Study.objects.get(pk=pk)
            return obj
        except Study.DoesNotExist:
            raise Http404
        except Exception as error:
            return {'error': f'The following error has occurred: {error}'}
        
class PostStudyAPIView(CreateAPIView):
    __doc__ = f'''
    `[POST]`
    This API view inserts a study on the DataBase.
    '''
    queryset = Study.objects.all()
    serializer_class = StudySerializer
    permission_classes = [IsAuthenticated, IsAdminUser]
    
class UpdateStudyAPIView(UpdateAPIView):
    __doc__ = f'''
    `[PUT]`
    This API view updates a study.
    '''
    queryset = Study.objects.all()
    serializer_class = StudySerializer
    permission_classes = [IsAuthenticated, IsAdminUser]

class DestroyStudyAPIView(DestroyAPIView):
    __doc__ = f'''
    `[DELETE]`
    This API view deletes a study.
    '''
    queryset = Study.objects.all()
    serializer_class = StudySerializer
    permission_classes = [IsAuthenticated, IsAdminUser]

#NOTE: TECHNOLOGY VIEWS:
class GetTechnologyAPIView(ListAPIView):
    __doc__ = f'''
    `[GET]`
    This API view returns all the technologies.
    '''
    queryset = Technology.objects.all()
    serializer_class = TechnologySerializer
    permission_classes = [IsAuthenticated, IsAdminUser]
    
class GetSingleTechnologyAPIView(RetrieveAPIView):
    __doc__ = f'''
    `[GET]`
    This API view returns a single technology.
    '''
    serializer_class = TechnologySerializer
    permission_classes = [IsAuthenticated, IsAdminUser]

    def get_object(self):
        try:
            pk = self.kwargs['pk']
            obj = Technology.objects.get(pk=pk)
            return obj
        except Technology.DoesNotExist:
            raise Http404
        except Exception as error:
            return {'error': f'The following error has occurred: {error}'}
        
class PostTechnologyAPIView(CreateAPIView):
    __doc__ = f'''
    `[POST]`
    This API view inserts a technology on the DataBase.
    '''
    queryset = Technology.objects.all()
    serializer_class = TechnologySerializer
    permission_classes = [IsAuthenticated, IsAdminUser]
    
class UpdateTechnologyAPIView(UpdateAPIView):
    __doc__ = f'''
    `[PUT]`
    This API view updates a technology.
    '''
    queryset = Technology.objects.all()
    serializer_class = TechnologySerializer
    permission_classes = [IsAuthenticated, IsAdminUser]

class DestroyTechnologyAPIView(DestroyAPIView):
    __doc__ = f'''
    `[DELETE]`
    This API view deletes a technology.
    '''
    queryset = Technology.objects.all()
    serializer_class = TechnologySerializer
    permission_classes = [IsAuthenticated, IsAdminUser]

#NOTE: VALIDATION VIEWS:
class GetValidationAPIView(ListAPIView):
    __doc__ = f'''
    `[GET]`
    This API view returns all the users' validations for all technologies and studies.
    '''
    queryset = Validation.objects.all()
    serializer_class = ValidationSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]
    
class GetSingleValidationAPIView(RetrieveAPIView):
    __doc__ = f'''
    `[GET]`
    This API view returns a single validation.
    '''
    serializer_class = ValidationSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]

    def get_object(self):
        try:
            pk = self.kwargs['pk']
            obj = Validation.objects.get(pk=pk)
            return obj
        except Validation.DoesNotExist:
            raise Http404
        except Exception as error:
            return {'error': f'The following error has occurred: {error}'}
        
class PostValidationAPIView(CreateAPIView):
    __doc__ = f'''
    `[POST]`
    This API view inserts a validation for a related technology or study on the DataBase.
    '''
    queryset = Validation.objects.all()
    serializer_class = ValidationSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]
    
class UpdateValidationAPIView(UpdateAPIView):
    __doc__ = f'''
    `[PUT]`
    This API view updates a validation.
    '''
    queryset = Validation.objects.all()
    serializer_class = ValidationSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]

class DestroyValidationAPIView(DestroyAPIView):
    __doc__ = f'''
    `[DELETE]`
    This API view deletes a validation.
    '''
    queryset = Validation.objects.all()
    serializer_class = ValidationSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]