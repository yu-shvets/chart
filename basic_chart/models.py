from django.db import models

# Create your models here.


class Region(models.Model):

    class Meta(object):
        verbose_name = 'Група'
        verbose_name_plural = 'Групы'

    region = models.CharField(
        primary_key=True,
        max_length=40,
        verbose_name='Регион'
    )

    def __str__(self):
        return "{}".format(self.region)


class Data(models.Model):

    class Meta(object):
        verbose_name = 'Данные'
        verbose_name_plural = 'Данные'

    region = models.ForeignKey(Region, verbose_name='Регион')

    country = models.CharField(
        max_length=40,
        verbose_name='Страна'
    )

    rate = models.FloatField(
        verbose_name='Значение'
    )

    def __str__(self):
        return "{}".format(self.country)
