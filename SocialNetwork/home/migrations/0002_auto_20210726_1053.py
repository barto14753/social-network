# Generated by Django 3.2.5 on 2021-07-26 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='photo',
            field=models.BinaryField(blank=True, null=True),
        ),
    ]
