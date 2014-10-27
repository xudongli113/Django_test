from django.core.mail import send_mail

send_mail('django test', 'play with send email.', 'vampirelee113@gmail.com',
    ['vampirelee113@example.com'], fail_silently=False)

