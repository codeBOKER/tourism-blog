# Generated by Django 4.2.9 on 2024-03-19 23:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0021_remove_comment_cmtimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='CMTimage',
            field=models.ImageField(blank=True, null=True, upload_to='users_photo/%y/%m/%d'),
        ),
    ]
