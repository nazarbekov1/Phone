from django.contrib.auth.models import User
from django.db import models

from characteristic_app.models import Display, NetworkSupport, Camera, ComputingResources, Battery,\
    SecureAuthentication,\
    DisplayAndBody, WaterAndDustProtection, DimensionsAndWeight, AudiAndVideo, ContentsOfDelivery


class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return f'{self.name}'


class Color(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        verbose_name = 'Цвет'
        verbose_name_plural = 'Цвета'

    def __str__(self):
        return self.title


class Phone(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)

    a = '64'
    b = '128'
    c = '254'
    d = '508'
    memory = [
        (a, '64'),
        (b, '128'),
        (c, '254'),
        (d, '508'), ]
    memory = models.CharField(max_length=3, choices=memory, null=True, default=None)
    color = models.ForeignKey(Color, on_delete=models.PROTECT)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.PROTECT)

    display = models.ForeignKey(Display,
                                on_delete=models.PROTECT, verbose_name='Дисплей')
    network_support = models.ForeignKey(NetworkSupport,
                                        on_delete=models.PROTECT, verbose_name='Поддержка сетей')
    camera = models.ForeignKey(Camera,
                               on_delete=models.PROTECT, verbose_name='Камера')
    computing_resources = models.ForeignKey(ComputingResources,
                                            on_delete=models.PROTECT, verbose_name='Вычислительные ресурсы')
    battery = models.ForeignKey(Battery,
                                on_delete=models.PROTECT, verbose_name='Аккумулятор')
    secure_authentication = models.ForeignKey(SecureAuthentication,
                                              on_delete=models.PROTECT, verbose_name='Безопасная аутентификация')
    display_and_body = models.ForeignKey(DisplayAndBody,
                                         on_delete=models.PROTECT, verbose_name='Дисплей и корпус')
    water_and_dust_protection = models.ForeignKey(WaterAndDustProtection,
                                                  on_delete=models.PROTECT, verbose_name='Защита от воды и пыли')
    audi_and_video = models.ForeignKey(AudiAndVideo,
                                       on_delete=models.PROTECT, verbose_name='Аудио и видео')
    dimensions_and_weight = models.ForeignKey(DimensionsAndWeight,
                                              on_delete=models.PROTECT, verbose_name='Размеры и вес')
    contents_of_delivery = models.ForeignKey(ContentsOfDelivery,
                                             on_delete=models.PROTECT, verbose_name='Комплект поставки')
    photo = models.ImageField(upload_to='media', blank=True)

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return self.name


class PhoneImage(models.Model):
    """Фото объекта"""
    image = models.ImageField(verbose_name='Фото')
    image_link = models.ForeignKey(Phone, verbose_name='Ссылка на объект', on_delete=models.CASCADE,
                                   related_name='image')

    class Meta:
        verbose_name = 'Фото объекта'
        verbose_name_plural = 'Фото объекта'




