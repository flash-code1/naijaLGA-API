# Generated by Django 2.0 on 2018-07-24 02:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('state', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='state',
            name='population',
            field=models.IntegerField(default=12),
            preserve_default=False,
        ),
    ]