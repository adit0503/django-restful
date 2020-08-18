# Generated by Django 2.1.4 on 2020-08-18 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_timestamp', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(default='', max_length=120)),
                ('release_date', models.DateTimeField()),
                ('esrb_rating', models.CharField(default='', max_length=1250)),
                ('played_once', models.BooleanField(default=False)),
                ('payed_times', models.IntegerField(default=0)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]