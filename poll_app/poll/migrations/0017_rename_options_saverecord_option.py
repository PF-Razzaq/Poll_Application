# Generated by Django 4.2.7 on 2024-01-24 12:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0016_saverecord_delete_polloption_delete_pollquestion'),
    ]

    operations = [
        migrations.RenameField(
            model_name='saverecord',
            old_name='options',
            new_name='option',
        ),
    ]