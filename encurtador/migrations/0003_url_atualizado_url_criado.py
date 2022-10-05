# Generated by Django 4.0.6 on 2022-10-05 19:36

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('encurtador', '0002_url_shortcode'),
    ]

    operations = [
        migrations.AddField(
            model_name='url',
            name='atualizado',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='url',
            name='criado',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
