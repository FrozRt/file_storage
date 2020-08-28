# Generated by Django 3.1 on 2020-08-28 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('file_handler_app', '0009_auto_20200828_1128'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='data',
            name='file_hash',
        ),
        migrations.AddField(
            model_name='data',
            name='hash_name',
            field=models.CharField(default='Null', max_length=256, verbose_name='e'),
        ),
    ]