# Generated by Django 4.2.11 on 2024-03-27 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0031_testimonial_tmldate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='BLGimage',
            field=models.ImageField(upload_to='media/images/%y/%m/%d', verbose_name='blog image'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='CMTimage',
            field=models.ImageField(blank=True, null=True, upload_to='media/users_photo/%y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='paragraph',
            name='PARimage',
            field=models.ImageField(blank=True, null=True, upload_to='media/images/%y/%m/%d', verbose_name='blog image'),
        ),
        migrations.AlterField(
            model_name='testimonial',
            name='TMLimage',
            field=models.ImageField(upload_to='media/users_photo/experiance/%y/%m/%d', verbose_name='photo'),
        ),
        migrations.AlterField(
            model_name='writer',
            name='WRTRimage',
            field=models.ImageField(blank=True, null=True, upload_to='media/writer/%y/%m/%d', verbose_name='photo'),
        ),
    ]
