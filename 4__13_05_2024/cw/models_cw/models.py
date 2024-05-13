from django.db import models


# Create your models here.


class Human(models.Model):
    GENDER = (
        ('м', 'муж.'),
        ('ж', 'жен.')
    )

    name = models.CharField(max_length=25)
    surname = models.CharField(max_length=25)
    age = models.IntegerField()
    gender = models.CharField(max_length=1, choices=GENDER)

    class Meta:
        verbose_name = 'Человек'
        verbose_name_plural = 'Люди'
        ordering = ['id']

    def __str__(self):
        return self.name


class Child(models.Model):
    GENDER = (
        ('м', 'муж.'),
        ('ж', 'жен.')
    )

    name = models.CharField(max_length=25)
    surname = models.CharField(max_length=25)
    age = models.IntegerField()
    gender = models.CharField(max_length=1, choices=GENDER)
    father = models.OneToOneField(Human, related_name='father', on_delete=models.SET_NULL, null=True, blank=True)
    mother = models.OneToOneField(Human, related_name='mother', on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        verbose_name = 'Ребёнок'
        verbose_name_plural = 'Дети'
        ordering = ['id']

    def __str__(self):
        return self.name


class IceCream(models.Model):
    name = models.CharField(max_length=25)
    price = models.DecimalField(max_digits=5, decimal_places=4)

    class Meta:
        verbose_name = 'Мороженное'
        verbose_name_plural = 'Мороженное'
        ordering = ['id']

    def __str__(self):
        return self.name


class Kiosk(models.Model):
    name = models.CharField(max_length=25)
    ice_cream = models.OneToOneField(IceCream, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        verbose_name = 'Киоск'
        verbose_name_plural = 'Киоски'
        ordering = ['id']

    def __str__(self):
        return self.name