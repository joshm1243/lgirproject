# Generated by Django 3.1.4 on 2021-02-09 17:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Account',
            new_name='Profiles',
        ),
    ]