# Generated by Django 4.2.11 on 2024-03-15 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='BLGdate',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Date'),
        ),
    ]
