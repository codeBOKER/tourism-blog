# Generated by Django 4.2.11 on 2024-03-24 23:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0029_message'),
    ]

    operations = [
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TMLname', models.CharField(max_length=50, verbose_name='name')),
                ('TMLexperiance', models.TextField(verbose_name='experiance')),
                ('TMLimage', models.ImageField(upload_to='users_photo/experiance/%y/%m/%d', verbose_name='photo')),
            ],
        ),
    ]
