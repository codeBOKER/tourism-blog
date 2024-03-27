# Generated by Django 4.2.9 on 2024-03-22 23:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0028_alter_writer_wrtrimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('MSGname', models.CharField(max_length=50, verbose_name='name')),
                ('MSGemail', models.EmailField(max_length=254, verbose_name='email')),
                ('MSGsubject', models.CharField(max_length=50, verbose_name='subject')),
                ('MSGmessage', models.TextField(verbose_name='message')),
            ],
        ),
    ]
