# Generated by Django 3.1.4 on 2020-12-18 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administration', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='admin_staff',
            name='age',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]