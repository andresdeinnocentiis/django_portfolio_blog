from django.apps import AppConfig


class UserProfileConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'UserProfile'
    
    #NOTE: When the object is created and ready, it calls the signals of the model and triggers whatever Signal is set. 
    def ready(self):
        import UserProfile.signals




    