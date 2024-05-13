import uuid

from django.db import models


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Post(models.Model):
    STATUS_CHOICES = (
        ('n', 'New'),
        ('o', 'Old'),
        ('d', 'Deleted')
    )

    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255, db_index=True,
                             unique_for_date='published')  # уникальная по этому полю на день
    description = models.CharField(max_length=255, blank=True, null=True)
    content = models.TextField(null=True, blank=True)
    published = models.DateTimeField(auto_now_add=True)  # , db_column="published_at" переименовывает поле в db\
    post_is_active = models.BooleanField(default=False)
    rating = models.DecimalField(max_digits=2, decimal_places=1)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)
    category = models.ForeignKey(Category, related_name='posts',
                                 on_delete=models.CASCADE)  # , to_field='столбец' , on_delete = models.Set('value')

    # temp = models.OneToOneField() #связь один к одному
    # temp = models.ManyToManyField() #связь многие ко многим

    class Meta:
        verbose_name = 'Статью'
        verbose_name_plural = 'Статьи'
        ordering = ['id']

    def __str__(self):
        return self.title
