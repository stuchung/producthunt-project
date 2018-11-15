# Generated by Django 2.1.2 on 2018-11-15 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20181115_1557'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='body',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='title',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='product',
            name='votes_total',
            field=models.IntegerField(default=1),
        ),
    ]