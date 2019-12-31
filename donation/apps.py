from django.apps import AppConfig

class DonationConfig(AppConfig):
    name = 'donation'
    
    def ready(self):
        import donation.handlers
        import donation.signals
        import donation.signals.signals
        import donation.signals.handlers
