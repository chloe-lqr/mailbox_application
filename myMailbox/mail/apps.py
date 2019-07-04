from django.apps import AppConfig


class MailConfig(AppConfig):
    name = 'mail'
    def ready(self):
        #print(self.name)
        import mail.signal
