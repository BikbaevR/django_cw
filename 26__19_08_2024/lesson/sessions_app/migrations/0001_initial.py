# Generated by Django 4.2.15 on 2024-08-19 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MainUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('is_admin', models.BooleanField(default=False)),
                ('token', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
