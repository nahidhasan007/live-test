# Generated by Django 3.1.2 on 2021-05-03 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BekarJubok', '0002_auto_20210502_2344'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('occupation', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('profile_pic', models.ImageField(blank=True, null=True, upload_to='profils_pics/')),
            ],
        ),
    ]