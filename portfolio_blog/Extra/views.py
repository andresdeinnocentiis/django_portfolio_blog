from django.shortcuts import render, redirect
from django.http import Http404
from .models import Study, Technology, Validation
from .forms import AddStudyForm, AddTechnologyForm

# Para Autenticar con JWT Token:
from rest_framework_simplejwt.authentication import JWTAuthentication

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


#NOTE: STUDY VIEWS:
class GetStudysAPIView(ListAPIView):
    __doc__ = f'''
    `[GET]`
    This API view returns all the studies.
    '''
    queryset = Study.objects.all()
    serializer_class = StudySerializer

    
class GetSingleStudyAPIView(RetrieveAPIView):
    __doc__ = f'''
    `[GET]`
    This API view returns a single study.
    '''
    serializer_class = StudySerializer
    permission_classes = [IsAuthenticated, IsAdminUser]
    # Agregamos esta autenticación para poder mandar requests a la API teniendo instalado Simple JWT Token
    authentication_classes = [JWTAuthentication]

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
    # Agregamos esta autenticación para poder mandar requests a la API teniendo instalado Simple JWT Token
    authentication_classes = [JWTAuthentication]
    
class UpdateStudyAPIView(UpdateAPIView):
    __doc__ = f'''
    `[PUT]`
    This API view updates a study.
    '''
    queryset = Study.objects.all()
    serializer_class = StudySerializer
    permission_classes = [IsAuthenticated, IsAdminUser]
    # Agregamos esta autenticación para poder mandar requests a la API teniendo instalado Simple JWT Token
    authentication_classes = [JWTAuthentication]

class DestroyStudyAPIView(DestroyAPIView):
    __doc__ = f'''
    `[DELETE]`
    This API view deletes a study.
    '''
    queryset = Study.objects.all()
    serializer_class = StudySerializer
    permission_classes = [IsAuthenticated, IsAdminUser]
    # Agregamos esta autenticación para poder mandar requests a la API teniendo instalado Simple JWT Token
    authentication_classes = [JWTAuthentication]

#NOTE: TECHNOLOGY VIEWS:
class GetTechnologysAPIView(ListAPIView):
    __doc__ = f'''
    `[GET]`
    This API view returns all the technologies.
    '''
    queryset = Technology.objects.all()
    serializer_class = TechnologySerializer
    # permission_classes = [IsAuthenticated, IsAdminUser]
    # # Agregamos esta autenticación para poder mandar requests a la API teniendo instalado Simple JWT Token
    # authentication_classes = [JWTAuthentication]
    
class GetSingleTechnologyAPIView(RetrieveAPIView):
    __doc__ = f'''
    `[GET]`
    This API view returns a single technology.
    '''
    serializer_class = TechnologySerializer
    permission_classes = [IsAuthenticated, IsAdminUser]
    # Agregamos esta autenticación para poder mandar requests a la API teniendo instalado Simple JWT Token
    authentication_classes = [JWTAuthentication]

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
    # Agregamos esta autenticación para poder mandar requests a la API teniendo instalado Simple JWT Token
    authentication_classes = [JWTAuthentication]
    
class UpdateTechnologyAPIView(UpdateAPIView):
    __doc__ = f'''
    `[PUT]`
    This API view updates a technology.
    '''
    queryset = Technology.objects.all()
    serializer_class = TechnologySerializer
    permission_classes = [IsAuthenticated, IsAdminUser]
    # Agregamos esta autenticación para poder mandar requests a la API teniendo instalado Simple JWT Token
    authentication_classes = [JWTAuthentication]

class DestroyTechnologyAPIView(DestroyAPIView):
    __doc__ = f'''
    `[DELETE]`
    This API view deletes a technology.
    '''
    queryset = Technology.objects.all()
    serializer_class = TechnologySerializer
    permission_classes = [IsAuthenticated, IsAdminUser]
    # Agregamos esta autenticación para poder mandar requests a la API teniendo instalado Simple JWT Token
    authentication_classes = [JWTAuthentication]




#NOTE: VALIDATION VIEWS:
class GetValidationsAPIView(ListAPIView):
    __doc__ = f'''
    `[GET]`
    This API view returns all the users' validations for all technologies and studies.
    '''
    queryset = Validation.objects.all()
    serializer_class = ValidationSerializer

    
class GetSingleValidationAPIView(RetrieveAPIView):
    __doc__ = f'''
    `[GET]`
    This API view returns a single validation.
    '''
    serializer_class = ValidationSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]
    # Agregamos esta autenticación para poder mandar requests a la API teniendo instalado Simple JWT Token
    authentication_classes = [JWTAuthentication]

    def get_object(self):
        try:
            pk = self.kwargs['pk']
            obj = Validation.objects.get(pk=pk)
            return obj
        except Validation.DoesNotExist:
            raise Http404
        except Exception as error:
            return {'error': f'The following error has occurred: {error}'}
        

class GetUserValidationForTechnologyAPIView(ListAPIView):
    __doc__ = f'''
    `[GET]`
    This API view returns the user Validation for a determined Technology.
    '''
    serializer_class = ValidationSerializer
    
    queryset = Validation.objects.all()

    def get_queryset(self):
        try:
            skillId = self.kwargs['skillId']
            identifier = self.kwargs['identifier']

            validations_x_tech = self.queryset.filter(technology=skillId)
            user_Validation_x_tech = validations_x_tech.filter(user=identifier)
            
            return user_Validation_x_tech

        except Validation.DoesNotExist:
            raise Http404
        except Exception as error:
            return {'error': f'The following error has occurred: {error}'}

class GetAnonUserValidationForTechnologyAPIView(ListAPIView):
    __doc__ = f'''
    `[GET]`
    This API view returns the anonymous user like for a determined review.
    '''
    serializer_class = ValidationSerializer
    
    queryset = Validation.objects.all()

    def get_queryset(self):
        try:
            skillId = self.kwargs['skillId']
            identifier = self.kwargs['identifier']

            validations_x_tech = self.queryset.filter(technology=skillId)
            user_Validation_x_tech = validations_x_tech.filter(anonymous_identifier=identifier)
            
            return user_Validation_x_tech

        except Validation.DoesNotExist:
            raise Http404
        except Exception as error:
            return {'error': f'The following error has occurred: {error}'}
        
        

class GetUserValidationForStudyAPIView(ListAPIView):
    __doc__ = f'''
    `[GET]`
    This API view returns the user Validation for a determined Study.
    '''
    serializer_class = ValidationSerializer
    
    queryset = Validation.objects.all()

    def get_queryset(self):
        try:
            studyId = self.kwargs['studyId']
            identifier = self.kwargs['identifier']

            validations_x_study = self.queryset.filter(study=studyId)
            user_validation_x_study = validations_x_study.filter(user=identifier)
            
            return user_validation_x_study

        except Validation.DoesNotExist:
            raise Http404
        except Exception as error:
            return {'error': f'The following error has occurred: {error}'}

class GetAnonUserValidationForStudyAPIView(ListAPIView):
    __doc__ = f'''
    `[GET]`
    This API view returns the anonymous user like for a determined review.
    '''
    serializer_class = ValidationSerializer
    
    queryset = Validation.objects.all()

    def get_queryset(self):
        try:
            studyId = self.kwargs['studyId']
            identifier = self.kwargs['identifier']

            validations_x_study = self.queryset.filter(study=studyId)
            user_validation_x_study = validations_x_study.filter(anonymous_identifier=identifier)
            
            return user_validation_x_study

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
    # permission_classes = [IsAuthenticated, IsAdminUser] # Lo dejo comentado porque supongo que todos los usuarios deben poder validar una tech o study
    # # Agregamos esta autenticación para poder mandar requests a la API teniendo instalado Simple JWT Token
    # authentication_classes = [JWTAuthentication] # Lo dejo comentado porque supongo que todos los usuarios deben poder validar una tech o study
    
class UpdateValidationAPIView(UpdateAPIView):
    __doc__ = f'''
    `[PUT]`
    This API view updates a validation.
    '''
    queryset = Validation.objects.all()
    serializer_class = ValidationSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]
    # Agregamos esta autenticación para poder mandar requests a la API teniendo instalado Simple JWT Token
    authentication_classes = [JWTAuthentication]

class DestroyValidationAPIView(DestroyAPIView):
    __doc__ = f'''
    `[DELETE]`
    This API view deletes a validation.
    '''
    queryset = Validation.objects.all()
    serializer_class = ValidationSerializer
    # permission_classes = [IsAuthenticated, IsAdminUser] # Lo dejo comentado porque supongo que todos los usuarios deben poder remover su validacion
    # # Agregamos esta autenticación para poder mandar requests a la API teniendo instalado Simple JWT Token
    # authentication_classes = [JWTAuthentication] # Lo dejo comentado porque supongo que todos los usuarios deben poder remover su validacion