# Generated by Django 5.0.4 on 2024-04-30 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('short_description', models.TextField()),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='about')),
            ],
            options={
                'verbose_name': 'About me',
                'verbose_name_plural': 'About me',
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Service name')),
                ('description', models.TextField(verbose_name='About Service')),
            ],
        ),
    ]
