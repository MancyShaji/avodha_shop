# Generated by Django 3.2.6 on 2021-11-30 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0004_alter_cartlist_cart_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartlist',
            name='cart_id',
            field=models.CharField(max_length=250, unique=True),
        ),
    ]
