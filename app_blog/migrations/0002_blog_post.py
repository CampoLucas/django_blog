# Generated by Django 4.1.7 on 2023-03-05 17:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('subtitle', models.CharField(blank=True, max_length=100)),
                ('description', models.TextField(blank=True, max_length=600)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('url', models.SlugField(editable=False, max_length=200, unique=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='author', to='app_blog.bloguser')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('body', models.TextField()),
                ('date_posted', models.DateTimeField(auto_now_add=True)),
                ('url', models.SlugField(editable=False, max_length=200, unique=True)),
                ('state', models.BooleanField(choices=[(True, 'Published'), (False, 'Draft')], default=False)),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='related_posts', to='app_blog.blog')),
            ],
        ),
    ]
