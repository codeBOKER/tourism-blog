# Generated by Django 4.2.9 on 2024-03-17 23:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_userdata'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userdata',
            old_name='CMTdate',
            new_name='UDdate',
        ),
        migrations.RenameField(
            model_name='userdata',
            old_name='CMTemail',
            new_name='UDemail',
        ),
        migrations.RenameField(
            model_name='userdata',
            old_name='PARimage',
            new_name='UDimage',
        ),
    ]
