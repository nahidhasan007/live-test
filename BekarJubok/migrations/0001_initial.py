# Generated by Django 3.1.2 on 2021-05-05 06:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('occupation', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('profile_pic', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='JobCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=100)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='JObDescription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(default='Google', max_length=200)),
                ('position', models.CharField(default='Software Engineer', max_length=200)),
                ('desc', models.TextField()),
                ('experience', models.TextField()),
                ('skills', models.TextField()),
                ('app_dedline', models.TextField()),
                ('published', models.DateTimeField()),
                ('jobcategory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category', to='BekarJubok.jobcategory')),
            ],
        ),
    ]
