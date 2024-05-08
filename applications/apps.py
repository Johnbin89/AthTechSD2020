from django.apps import AppConfig


class ApplicationsConfig(AppConfig):
    name = 'applications'

    def ready(self):
        # Implicitly connect signal handlers decorated with @receiver.
        import applications.signals