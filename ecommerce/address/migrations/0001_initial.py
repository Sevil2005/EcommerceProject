# Generated by Django 2.2.3 on 2021-02-25 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=30, null=True)),
                ('nickname', models.CharField(blank=True, max_length=30, null=True)),
                ('address_type', models.CharField(choices=[('billing', 'Billing Address'), ('shipping', 'Shipping Address')], max_length=30)),
                ('address_line_1', models.CharField(blank=True, max_length=50, null=True)),
                ('address_line_2', models.CharField(blank=True, max_length=50, null=True)),
                ('city', models.CharField(blank=True, max_length=50, null=True)),
                ('country', models.CharField(blank=True, max_length=50, null=True)),
                ('state', models.CharField(blank=True, max_length=50, null=True)),
                ('postal_code', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
    ]
