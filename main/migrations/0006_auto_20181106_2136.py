# Generated by Django 2.0.9 on 2018-11-06 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_post_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='Lat',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='Lng',
            field=models.FloatField(null=True),
        ),
    ]
