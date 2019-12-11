from django.apps import AppConfig

print("100000")

class DonationConfig(AppConfig):
    name = 'donation'

    def ready(self):
        import donation.handlers
        import donation.signals
        import donation.signals.signals
        import donation.signals.handlers