# Generated by Django 3.1.4 on 2020-12-18 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='students',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='students',
            name='phone_number',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='students',
            name='student_email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]
