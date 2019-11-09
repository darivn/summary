# Generated by Django 2.2.6 on 2019-11-09 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Backgrounds',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('institution_name', models.CharField(max_length=300)),
                ('city', models.CharField(max_length=100)),
                ('faculty', models.CharField(max_length=300)),
                ('specialization', models.CharField(max_length=200)),
                ('level', models.CharField(max_length=150)),
                ('year_start', models.IntegerField()),
                ('year_end', models.IntegerField()),
            ],
        ),
    ]
