# Generated by Django 2.2.9 on 2020-01-21 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('updates', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='update',
            name='content',
            field=models.TextField(blank=True, null=True),
        ),
    ]