# Generated by Django 3.1 on 2020-08-28 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('file_handler_app', '0006_auto_20200828_1108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='file_name_hash',
            field=models.CharField(max_length=256, verbose_name='6eef6648406c333a4035cd5e60d0bf2ecf2606d7'),
        ),
    ]
