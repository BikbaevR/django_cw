# Generated by Django 4.2.13 on 2024-06-05 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0003_alter_book_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='image',
            field=models.ImageField(upload_to='books/%d-%m-%y'),
        ),
    ]
