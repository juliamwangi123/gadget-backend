from django.apps import AppConfig


class GadgethubConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'gadgethub'
    
    
    def ready(self):
        
        import gadgethub.signals
        
