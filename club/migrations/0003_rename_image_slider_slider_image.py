# Generated by Django 4.0.5 on 2023-07-07 07:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('club', '0002_homeslider'),
    ]

    operations = [
        migrations.RenameField(
            model_name='slider',
            old_name='image',
            new_name='slider_image',
        ),
    ]