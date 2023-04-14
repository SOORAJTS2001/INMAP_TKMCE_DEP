# Generated by Django 4.0.3 on 2023-04-14 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inmapapi', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='imagemodel',
            name='image',
        ),
        migrations.AddField(
            model_name='imagemodel',
            name='image_url',
            field=models.URLField(default='this is a default value'),
        ),
    ]
