# Generated by Django 4.1.7 on 2023-03-07 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_blog', '0005_rename_dysplay_name_bloguser_display_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bloguser',
            name='date_registered',
        ),
        migrations.AlterField(
            model_name='bloguser',
            name='date_joined',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
