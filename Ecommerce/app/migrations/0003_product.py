# Generated by Django 4.1.5 on 2023-02-06 02:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_rename_massage_person_message'),
    ]

    operations = [
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('discrition', models.TextField()),
                ('upload_img', models.ImageField(upload_to='product/')),
            ],
        ),
    ]
