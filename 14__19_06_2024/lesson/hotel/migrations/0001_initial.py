# Generated by Django 4.2.13 on 2024-06-19 15:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='HotelRoom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('price', models.FloatField()),
                ('description', models.TextField()),
                ('photo', models.ImageField(default='hotel/default.jpg', upload_to='hotel')),
            ],
        ),
        migrations.CreateModel(
            name='RoomType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_start', models.DateField()),
                ('date_end', models.DateField()),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotel.hotelroom')),
                ('user', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='hotelroom',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotel.roomtype'),
        ),
    ]
