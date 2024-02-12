from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Название')
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')

    class Meta:
        db_table = 'category'  # значение(имя) таблицы
        verbose_name = 'Категорию'  # название(полей ренейм их)
        verbose_name_plural = 'Категории'  # (ренейм для множественного числа)


    def __str__(self):
        return self.name


class Products(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Название')
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')
    description = models.TextField(max_length=300, blank=True, null=True, verbose_name='Описание')
    img = models.ImageField(upload_to='products_images', blank=True, null=True, verbose_name='Изображение')
    price = models.DecimalField(default=0.00, max_digits=7, decimal_places=2, verbose_name='Цена')
    discount = models.DecimalField(default=0.00, max_digits=7, decimal_places=2, verbose_name='Скидка в %')
    quantity = models.PositiveIntegerField(default=0, verbose_name='Количество')
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE, verbose_name='Категория')
    # Protect - если на категорию привязан хоть 1 не удалит
    # CASCADE - при удалении категории удаляются и закрепленные товары
    # SETDEFAULT - дефолт значение при удалении
    class Meta:
        db_table = 'product'  # значение(имя) таблицы
        verbose_name = 'Продукт'  # название(полей ренейм их)
        verbose_name_plural = 'Продукты'  # (ренейм для множественного числа)
        ordering: ("id",)


    def __str__(self):
        return f"{self.name} Количество - {self.quantity}"

    def display_id(self):
        return f"{self.id:05}"

    def sell_price(self):
        if self.discount:
            return round(self.price - (self.price * self.discount) / 100, 2)
        return self.price