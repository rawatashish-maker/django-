# Generated by Django 3.1.3 on 2020-11-30 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='address',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
        migrations.AddField(
            model_name='order',
            name='phone',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
    ]
