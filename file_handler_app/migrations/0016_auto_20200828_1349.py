# Generated by Django 3.1 on 2020-08-28 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('file_handler_app', '0015_auto_20200828_1348'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='hash_name',
            field=models.CharField(default='Null', max_length=256),
        ),
    ]
