# Generated by Django 4.1.7 on 2023-03-07 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_blog', '0008_alter_bloguser_display_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='image',
            field=models.ImageField(blank=True, upload_to='blog_pictures/'),
        ),
    ]
