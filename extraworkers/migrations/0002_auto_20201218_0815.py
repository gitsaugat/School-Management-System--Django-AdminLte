# Generated by Django 3.1.4 on 2020-12-18 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('extraworkers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extra_worker',
            name='image',
            field=models.ImageField(default='default.png', upload_to='extraworkers'),
        ),
    ]
