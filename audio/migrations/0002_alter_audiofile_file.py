# Generated by Django 5.0.6 on 2024-06-13 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('audio', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='audiofile',
            name='file',
            field=models.FileField(upload_to='audio/'),
        ),
    ]