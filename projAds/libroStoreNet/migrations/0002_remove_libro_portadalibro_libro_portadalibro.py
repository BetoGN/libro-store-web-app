# Generated by Django 5.0.6 on 2024-06-26 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libroStoreNet', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='libro',
            name='portadalibro',
        ),
        migrations.AddField(
            model_name='libro',
            name='portadaLibro',
            field=models.ImageField(blank=True, default='img/default.jpg', null=True, upload_to='img/'),
        ),
    ]
