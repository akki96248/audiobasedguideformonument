# Generated by Django 4.1.3 on 2023-03-14 18:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('audioguideapp', '0030_remove_guide_charges'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='guide',
            name='guide_date',
        ),
        migrations.RemoveField(
            model_name='guide',
            name='guide_time',
        ),
    ]