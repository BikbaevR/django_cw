from django.db import models
from django.core.exceptions import ValidationError


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


def validate_title(value):
    if value in ['slovo', 'plohoe']:
        raise ValidationError(message='Заголовок неправильный')


class Post(models.Model):
    title = models.CharField(max_length=100, validators=[validate_title])
    content = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


def validate_name(name: str):
    print(name)
    if 2 > len(name) > 100:
        raise ValidationError('Длина имени не верная')


def validate_age(age: int):
    if 12 > age > 100:
        raise ValidationError('Не верный возраст')


def validate_b_date(date):
    if date.year < 1900:
        raise ValidationError('Слишком старый')


class Users(models.Model):
    name = models.CharField(max_length=100, validators=[validate_name])
    age = models.IntegerField(validators=[validate_age])
    b_date = models.DateField(validators=[validate_b_date])

    def __str__(self):
        return self.name
