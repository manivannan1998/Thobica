# Generated by Django 3.1.7 on 2021-05-02 14:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0004_auto_20210502_0850'),
    ]

    operations = [
        migrations.RenameField(
            model_name='register',
            old_name='mail',
            new_name='email',
        ),
    ]
