# This Python file uses the following encoding: utf-8

from django.db import models

# Create your models here.

class Catch(models.Model):
    fish = models.CharField('Рыба', max_length=256)
    weight = models.DecimalField(max_digits=4,decimal_places=1)
    place = models.CharField(max_length=256)
    date  = models.DateField()
    time  = models.TimeField()
    depth = models.DecimalField(max_digits=4,decimal_places=1)

    lure_type_choices = (
        ('plug', 'воблер'),
        ('spoon', 'колебалка'),
        ('spinner', 'вертушка'),
        ('soft', 'силикон'),
    )
      

    lure_type  = models.CharField(choices = lure_type_choices,
                                 default = 'plug',
                                 max_length = 256)
    lure_model  = models.CharField(max_length=256)
    lure_size  = models.DecimalField(max_digits=4,decimal_places=1)
    lure_weight  = models.DecimalField(max_digits=4,decimal_places=1)
    lure_color = models.CharField(max_length=256)
    retrieve = models.TextField()
    note = models.TextField()


class Lure(models.Model):
    lure_type_choices = (
        ('plug', 'воблер'),
        ('spoon', 'колебалка'),
        ('spinner', 'вертушка'),
        ('soft', 'силикон'),
    )
      

    type  = models.CharField('Тип',choices = lure_type_choices,
                            default = 'plug',
                            max_length = 256)
    model  = models.CharField('Модель',default='-',max_length=256)
    manufacturer  = models.CharField('Марка',default='-',max_length=256)
    size  = models.DecimalField('Размер',default=0,max_digits=4,decimal_places=1)
    weight  = models.DecimalField('Вес',default=0,max_digits=4,decimal_places=1)
    max_depth = models.DecimalField('Глубина',default=0,max_digits=4,decimal_places=1)
    color = models.CharField('Цвет',default='-',max_length=256)
    have  = models.BooleanField('Есть',default=False,)
    note = models.TextField('Коментарий',default='',)
    link = models.URLField('web',default='')
