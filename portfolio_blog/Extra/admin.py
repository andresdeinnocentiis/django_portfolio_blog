from django.contrib import admin
from .models import Technology, Study, Validation

# Register your models here.

class TechnologyAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'years_exp', 'validations']

class StudyAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'institution', 'type', 'from_date', 'to_date', 'validations']

class ValidationAdmin(admin.ModelAdmin):
    list_display = ['id', 'user_username', 'anonymous_identifier', 'technology_name', 'study_name']
    
    def user_username(self, obj):
        return obj.user.username if obj.user else '-'
    
    def study_name(self, obj):
        try:
            return obj.study.name
        except:
            return "-"
        
    def technology_name(self, obj): 
        try:
            return obj.technology.name
        except:
            return "-"


admin.site.register(Study, StudyAdmin)
admin.site.register(Technology, TechnologyAdmin)
admin.site.register(Validation, ValidationAdmin)