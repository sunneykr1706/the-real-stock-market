# Generated by Django 3.0.4 on 2020-03-31 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('event', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.CharField(max_length=122)),
                ('time', models.CharField(max_length=122)),
                ('location', models.CharField(max_length=122)),
                ('img', models.CharField(max_length=122)),
                ('date', models.DateField()),
            ],
        ),
    ]
