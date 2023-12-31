# Generated by Django 4.1.7 on 2023-08-28 06:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_remove_userprofileinfo_username_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('city', models.CharField(blank=True, max_length=25, null=True)),
                ('media', models.FileField(blank=True, null=True, upload_to='article_pictures/')),
                ('user_profile_info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.userprofileinfo')),
            ],
        ),
    ]
