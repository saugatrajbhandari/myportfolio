# Generated by Django 4.0.3 on 2022-03-19 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0008_endorsement'),
    ]

    operations = [
        migrations.AddField(
            model_name='endorsement',
            name='approved',
            field=models.BooleanField(default=False),
        ),
    ]
