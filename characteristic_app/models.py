from django.db import models


class Display(models.Model):
    name = models.TextField()

    class Meta:
        verbose_name = 'Дисплей'
        verbose_name_plural = 'Дисплеи'

    def __str__(self):
        return self.name


class NetworkSupport (models.Model):
    name = models.TextField()

    class Meta:
        verbose_name = 'Поддержка сетей'
        verbose_name_plural = 'Поддержки сетей'

    def __str__(self):
        return self.name


class Camera(models.Model):
    name = models.TextField()

    class Meta:
        verbose_name = 'Камера'
        verbose_name_plural = 'Камеры'

    def __str__(self):
        return self.name


class ComputingResources(models.Model):
    name = models.TextField()

    class Meta:
        verbose_name = 'Вычислительные ресурсы'
        verbose_name_plural = 'Вычислительные ресурсы'

    def __str__(self):
        return self.name


class Battery(models.Model):
    name = models.TextField()

    class Meta:
        verbose_name = 'Аккумулятор'
        verbose_name_plural = 'Аккумуляторы'

    def __str__(self):
        return self.name


class SecureAuthentication(models.Model):
    name = models.TextField()

    class Meta:
        verbose_name = 'Безопасная аутентификация'
        verbose_name_plural = 'Безопасная аутентификация'

    def __str__(self):
        return self.name


class DisplayAndBody(models.Model):
    name = models.TextField()

    class Meta:
        verbose_name = 'Дисплей и корпус'
        verbose_name_plural = 'Дисплеи и корпусы'

    def __str__(self):
        return self.name


class WaterAndDustProtection(models.Model):
    name = models.TextField()

    class Meta:
        verbose_name = 'Защита от воды и пыли'
        verbose_name_plural = 'Защита от воды и пыли'

    def __str__(self):
        return self.name


class AudiAndVideo(models.Model):
    name = models.TextField()

    class Meta:
        verbose_name = 'Аудио и видео'
        verbose_name_plural = 'Аудио и видео'

    def __str__(self):
        return self.name


class DimensionsAndWeight(models.Model):
    name = models.TextField()

    class Meta:
        verbose_name = 'Размеры и вес'
        verbose_name_plural = 'Размеры и вес'

    def __str__(self):
        return self.name


class ContentsOfDelivery(models.Model):
    name = models.TextField()

    class Meta:
        verbose_name = 'Комплект поставки'
        verbose_name_plural = 'Комплекты поставки'

    def __str__(self):
        return self.name



