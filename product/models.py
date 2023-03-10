from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver
from product.tasks import send_product_news

User = get_user_model()

class Category(models.Model):
    title = models.SlugField(primary_key=True,unique=True)
    parent = models.ForeignKey('self',on_delete=models.CASCADE,related_name='categories',null=True,blank=True)

    def __str__(self):
        return f'{self.title}'

class Product(models.Model):
    owner = models.ForeignKey(User,on_delete=models.CASCADE,related_name='products')
    category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name='products')
    title = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    amount = models.PositiveIntegerField(default=1)
    image = models.ImageField(upload_to='products/')
    # music = models.FileField(upload_to='music/')

    def __str__(self):
        return f'{self.title}'

@receiver(post_save,sender=Product)
def post_product(sender,instance,created,**kwargs):
    if created:
        send_product_news.delay(instance.title,instance.price)