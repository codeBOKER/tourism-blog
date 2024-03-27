# Generated by Django 4.2.11 on 2024-03-15 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_alter_blog_blgdate'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='BLGheader',
            field=models.CharField(default=models.CharField(max_length=255), max_length=80),
        ),
        migrations.AlterField(
            model_name='blog',
            name='BLGdate',
            field=models.DateTimeField(verbose_name='Date'),
        ),
    ]
