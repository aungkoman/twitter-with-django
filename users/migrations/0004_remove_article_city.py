# Generated by Django 4.1.7 on 2023-08-28 06:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_article'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='city',
        ),
    ]
