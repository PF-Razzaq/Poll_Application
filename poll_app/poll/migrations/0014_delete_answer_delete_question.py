# Generated by Django 4.2.7 on 2024-01-23 13:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0013_question_answer'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Answer',
        ),
        migrations.DeleteModel(
            name='Question',
        ),
    ]
