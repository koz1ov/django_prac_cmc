# Generated by Django 3.1.1 on 2020-09-25 22:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0011_auto_20200925_2215'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shorturl',
            name='original_url',
            field=models.URLField(verbose_name='Original url'),
        ),
    ]