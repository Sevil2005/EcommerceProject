# Generated by Django 3.1.6 on 2021-03-03 16:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0007_auto_20210302_1133'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='product_brand',
        ),
    ]