# Generated by Django 4.2.9 on 2024-03-16 01:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_blog_blgheader_alter_blog_blgdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='BLGheader',
            field=models.CharField(max_length=80),
        ),
    ]
