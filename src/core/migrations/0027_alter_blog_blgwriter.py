# Generated by Django 4.2.9 on 2024-03-21 22:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0026_alter_blog_blgwriter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='BLGwriter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.writer', verbose_name='writer'),
        ),
    ]
