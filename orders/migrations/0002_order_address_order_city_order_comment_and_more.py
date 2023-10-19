# Generated by Django 4.2.3 on 2023-08-30 07:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0009_merge_20230821_0839"),
        ("orders", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="order",
            name="address",
            field=models.CharField(default=None, max_length=512, verbose_name="адрес"),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="order",
            name="city",
            field=models.CharField(default=None, max_length=255, verbose_name="город"),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="order",
            name="comment",
            field=models.CharField(
                blank=True,
                max_length=512,
                null=True,
                verbose_name="комментарий к заказу",
            ),
        ),
        migrations.AddField(
            model_name="orderitem",
            name="product_position",
            field=models.ForeignKey(
                default=None,
                on_delete=django.db.models.deletion.CASCADE,
                to="products.productposition",
                verbose_name="позиция товара",
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="order",
            name="payment",
            field=models.CharField(
                choices=[
                    ("online", "Онлайн картой"),
                    ("someone", "Онлайн со случайного чужого счета"),
                ],
                max_length=10,
                verbose_name="способ оплаты",
            ),
        ),
    ]