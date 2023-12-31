# Generated by Django 4.2.3 on 2023-08-17 16:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0007_merge_20230813_1438"),
    ]

    operations = [
        migrations.CreateModel(
            name="Seller",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("title", models.CharField(max_length=255, verbose_name="Название")),
                ("description", models.TextField(verbose_name="Описание")),
                ("image", models.ImageField(upload_to="sellers/", verbose_name="Изображение")),
                ("address", models.CharField(max_length=255, verbose_name="Адрес")),
                ("phone", models.CharField(max_length=20, verbose_name="Телефон")),
                ("email", models.EmailField(max_length=254, verbose_name="Email")),
                ("created", models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")),
                ("updated", models.DateTimeField(auto_now=True, verbose_name="Дата обновления")),
            ],
            options={
                "verbose_name": "Продавец",
                "verbose_name_plural": "Продавцы",
            },
        ),

        migrations.CreateModel(
            name="ProductPosition",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("price", models.DecimalField(decimal_places=2, max_digits=10, verbose_name="Цена")),
                ("quantity", models.PositiveIntegerField(verbose_name="Количество на складе")),
                ("created", models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")),
                ("updated", models.DateTimeField(auto_now=True, verbose_name="Дата обновления")),
                ("product", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="products.product",
                                              verbose_name="Товар")),
                ("seller", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="positions",
                                             to="products.seller", verbose_name="Продавец")),
            ],
            options={
                "verbose_name": "Товарная позиция",
                "verbose_name_plural": "Товарные позиции",
            },
        ),
    ]
