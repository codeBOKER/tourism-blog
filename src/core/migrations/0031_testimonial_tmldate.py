# Generated by Django 4.2.11 on 2024-03-24 23:25

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0030_testimonial'),
    ]

    operations = [
        migrations.AddField(
            model_name='testimonial',
            name='TMLdate',
            field=models.DateTimeField(auto_created=True, auto_now_add=True, default=django.utils.timezone.now, verbose_name='Date'),
            preserve_default=False,
        ),
    ]
