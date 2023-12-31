# Generated by Django 4.0.5 on 2023-07-07 05:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Club',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('reg_fee', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='upload/')),
            ],
        ),
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('image', models.ManyToManyField(to='club.image')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Registrations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('payment_number', models.CharField(max_length=50)),
                ('trx_id', models.CharField(max_length=50)),
                ('payment_method', models.CharField(choices=[('Bkash', 'Bkash'), ('Nagad', 'Nagad')], max_length=20)),
                ('payment_status', models.CharField(choices=[('Pending', 'Pending'), ('Completed', 'Completed')], max_length=20)),
                ('club', models.ManyToManyField(to='club.club')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField(max_length=50)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('details', models.URLField()),
                ('club', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='club.club')),
                ('image', models.ManyToManyField(to='club.image')),
            ],
        ),
        migrations.AddField(
            model_name='club',
            name='activities',
            field=models.ManyToManyField(to='club.image'),
        ),
        migrations.AddField(
            model_name='club',
            name='club_slider',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='club.slider'),
        ),
        migrations.AddField(
            model_name='club',
            name='members',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
