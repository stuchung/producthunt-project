# Generated by Django 2.1.2 on 2018-11-16 22:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_auto_20181116_1655'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='productname',
            new_name='title',
        ),
    ]