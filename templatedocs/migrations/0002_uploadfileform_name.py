# Generated by Django 3.2.16 on 2022-12-30 06:32

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('templatedocs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='uploadfileform',
            name='name',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
    ]
