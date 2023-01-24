from celery import shared_task
from django.core.mail import send_mail

@shared_task
def send_activation_code(email, activation_code):
    activation_link = f'http://35.185.69.40/account/activate/{activation_code}'
    message = f'Ваш заказ принят!\n{activation_link}'
    send_mail('Activate account', message, 'admin@admin.com', recipient_list=[email])
    return "Отправленно"