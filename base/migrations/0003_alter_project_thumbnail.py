# Generated by Django 4.0.3 on 2022-03-18 03:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='thumbnail',
            field=models.ImageField(default='images/project.jpg', upload_to=''),
        ),
    ]
