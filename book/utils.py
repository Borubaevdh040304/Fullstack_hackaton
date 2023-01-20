from django.core.mail import send_mail


def send_activation_mail(email, activation_code):
    activation_link = f'http://35.185.69.40/account/activate/{activation_code}/'
    message = f'Activate your account with a link:\n{activation_link}'
    send_mail("Activate account", message, 'admin@admin.com', recipient_list=[email], fail_silently=False)

