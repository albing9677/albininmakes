# Generated by Django 4.1.7 on 2023-03-24 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='stock',
            field=models.IntegerField(default=7822),
            preserve_default=False,
        ),
    ]