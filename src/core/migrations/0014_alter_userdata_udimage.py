# Generated by Django 4.2.9 on 2024-03-18 00:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_alter_userdata_udimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdata',
            name='UDimage',
            field=models.ImageField(default='\\static\\img\\default\\OIP.jpg', upload_to='users_photo/%y/%m/%d', verbose_name='users'),
        ),
    ]
