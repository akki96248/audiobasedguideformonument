# Generated by Django 4.1.3 on 2023-03-06 11:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('audioguideapp', '0012_remove_audio_file_path_remove_monument_info_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='audio',
            name='audio_language',
        ),
    ]