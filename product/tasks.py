from celery import shared_task
from django.core.mail import send_mail
from spam.models import Contact

@shared_task
def big_function():
    import time
    time.sleep(10)    

@shared_task 
def send_product_news(title,price):
    emails = [i.email for i in Contact.objects.all()]
    send_mail(
        'Py25 shop project', # title
        f'привет у нас новый товар {title} с ценой {price}', # body
        'imanaliev479125@gmail.com', # from
        emails # to

    )        
 