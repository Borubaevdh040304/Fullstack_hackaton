from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model
from .tasks import send_activation_code

User = get_user_model()


class Restaurant(models.Model):
    author = models.CharField(max_length=50)
    image = models.ImageField(upload_to='media', null=True, blank=True, default="")
    title = models.CharField(max_length=50)
    description = models.TextField()
    rating = models.IntegerField(default=0, help_text='Указывать рейтинг в integer')
    cuisine = models.CharField(max_length=50)
    work_time = models.CharField(max_length=250, null=True, blank=True)
    address = models.CharField(max_length=250)

    # def __str__(self) -> str:
    #     return self.title
    

    class Meta:
        verbose_name = "Ресторан"
        verbose_name_plural = "Рестораны"


class Post(models.Model):
    title = models.CharField(max_length=70, verbose_name='Название')
    image = models.ImageField(upload_to='media', null=True, blank=True, verbose_name='Изображение', default="")
    description = models.TextField(verbose_name='Описание')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    title_of_restourant = models.ForeignKey(Restaurant, related_name='restourant_name', on_delete=models.CASCADE, default="")
    post_category = models.CharField(max_length=50)

    TYPE = [
        ('BRK', 'Завтрак'),
        ('LUN', 'Обед'),
        ('DIN', 'Ужин'),
    ]

    type = models.CharField(choices=TYPE, max_length=3, default='BRK', verbose_name='Тип')


    # def __str__(self):
    #     return self.title
    
    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"


class Category(models.Model):
    cuisine = models.ForeignKey(Restaurant, related_name='rest_category', on_delete=models.SET_NULL, null=True, default="")
    category = models.ForeignKey(Post, related_name='post_categories', on_delete=models.CASCADE, default="")



class Orders(models.Model):
    users = models.ForeignKey(User, related_name='users_order', on_delete=models.SET_NULL, null=True)
    post_or = models.ForeignKey(Post, related_name='post_order', on_delete=models.SET_NULL, null=True)
    amount = models.IntegerField(default=0)
    name = models.CharField(max_length=90)
    email = models.CharField(max_length=111)
    address = models.CharField(max_length=111)
    city = models.CharField(max_length=111)
    phone = models.CharField(max_length=111, default="")
    timestamp = models.DateTimeField(default=timezone.now)
    
    def _create(self, email, password, **kwargs):
        if not email:
            raise ValueError("Email is required")
        email = self.normalize_email(email)
        # self.model == User
        user:User = self.model(email=email, **kwargs)
        user.set_password(password) # хеширует пароль
        user.create_activation_code()
        user.save(using=self._db) # сохраняем в бд
        send_activation_code.delay(user.email, user.activation_code)
        return user

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказ"
    
    def save(self, *args, **kwargs):
        super(Orders, self).save(*args, **kwargs)
    

def order_post_save(sender, instance, created, **kwargs):
    pass
    
# post


class History(models.Model):
    hist_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    post_id = models.CharField(max_length=10000000, default="")

    class Meta:
        verbose_name = "История"
        verbose_name_plural = "Истории"

# class Subscription(models.Model):
#     subscribe = models.ForeignKey(User, related_name='subscriptions', on_delete=models.CASCADE)
#     restourant = models.ForeignKey(Restaurant, related_name='subscribers', on_delete=models.CASCADE)


