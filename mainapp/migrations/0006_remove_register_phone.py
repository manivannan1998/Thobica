# Generated by Django 3.1.7 on 2021-05-02 15:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0005_auto_20210502_1024'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='register',
            name='phone',
        ),
    ]