# Generated by Django 3.1.7 on 2021-05-02 15:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0006_remove_register_phone'),
    ]

    operations = [
        migrations.RenameField(
            model_name='register',
            old_name='psw',
            new_name='password',
        ),
        migrations.RenameField(
            model_name='register',
            old_name='pswr',
            new_name='repeat_password',
        ),
    ]
