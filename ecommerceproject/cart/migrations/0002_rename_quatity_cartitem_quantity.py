# Generated by Django 4.1.7 on 2023-04-20 10:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cartitem',
            old_name='quatity',
            new_name='quantity',
        ),
    ]