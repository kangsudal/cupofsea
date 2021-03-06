# Generated by Django 2.0.9 on 2018-11-21 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20181106_2136'),
    ]

    operations = [
        migrations.CreateModel(
            name='Language_log',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kind', models.CharField(max_length=50)),
                ('who', models.CharField(max_length=50)),
                ('where', models.CharField(max_length=50)),
                ('startDate', models.DateTimeField(blank=True, null=True)),
                ('endDate', models.DateTimeField(blank=True, null=True)),
                ('topic', models.CharField(max_length=50)),
                ('summary', models.TextField()),
                ('what', models.CharField(max_length=50)),
            ],
        ),
    ]
