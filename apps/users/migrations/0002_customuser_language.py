# Generated by Django 3.2.16 on 2022-12-29 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='language',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
