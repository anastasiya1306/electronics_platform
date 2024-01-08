from django.db import models


class Provider(models.Model):
    name = models.CharField(max_length=75, verbose_name='Название')
    email = models.EmailField(unique=True, verbose_name='Почта')
    country = models.CharField(max_length=75, verbose_name='Страна')
    city = models.CharField(max_length=75, verbose_name='Город')
    street = models.CharField(max_length=75, verbose_name='Улица')
    house_number = models.CharField(max_length=100, verbose_name='Номер дома')
    arrears = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Задолженность')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Поставщик'
        verbose_name_plural = 'Поставщики'


class Network(models.Model):
    LEVEL_CHOICES = (
        (0, 'Завод'),
        (1, 'Розничная сеть'),
        (2, 'Индивидуальный предприниматель')
    )

    name = models.CharField(max_length=75, verbose_name='Название')
    email = models.EmailField(unique=True, verbose_name='Почта')
    country = models.CharField(max_length=75, verbose_name='Страна')
    city = models.CharField(max_length=75, verbose_name='Город')
    street = models.CharField(max_length=75, verbose_name='Улица')
    house_number = models.CharField(max_length=100, verbose_name='Номер дома')
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE, verbose_name='Поставщик')
    level = models.IntegerField(choices=LEVEL_CHOICES, verbose_name='Звено сети')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Поставщик'
        verbose_name_plural = 'Поставщики'


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    model = models.CharField(max_length=100, verbose_name='Модель')
    date_release = models.DateField(verbose_name='Дата выхода')
    network = models.ForeignKey(Network, on_delete=models.CASCADE, verbose_name='Звено сети')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания', null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
