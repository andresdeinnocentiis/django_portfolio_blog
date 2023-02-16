from django.urls import path
from .. import views


urlpatterns = [
    path('studies/', views.get_all_studies, name='all_studies'),
    path('studies/add', views.add_study, name='add_studiy'),
    
    path('technologies/', views.get_all_technologies, name='all_technologies'),
    path('technologies/add', views.add_technology, name='add_technology'),
    
]