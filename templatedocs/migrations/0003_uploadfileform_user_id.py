# Generated by Django 3.2.16 on 2023-01-03 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('templatedocs', '0002_uploadfileform_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='uploadfileform',
            name='user_id',
            field=models.IntegerField(default=0),
        ),
    ]
