# Generated by Django 5.0.1 on 2024-01-08 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Provider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=75, verbose_name='Название')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Почта')),
                ('country', models.CharField(max_length=75, verbose_name='Страна')),
                ('city', models.CharField(max_length=75, verbose_name='Город')),
                ('street', models.CharField(max_length=75, verbose_name='Улица')),
                ('house_number', models.CharField(max_length=100, verbose_name='Номер дома')),
                ('arrears', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Задолженность')),
            ],
            options={
                'verbose_name': 'Поставщик',
                'verbose_name_plural': 'Поставщики',
            },
        ),
    ]
