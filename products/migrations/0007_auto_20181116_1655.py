# Generated by Django 2.1.2 on 2018-11-16 21:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_auto_20181116_1021'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='name',
            new_name='productname',
        ),
    ]