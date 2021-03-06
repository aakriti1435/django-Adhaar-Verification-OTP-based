# Generated by Django 2.0.6 on 2020-03-22 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DummyAadharData',
            fields=[
                ('person_id', models.AutoField(primary_key=True, serialize=False)),
                ('firt_name', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('last_name', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('date_of_birth', models.DateField()),
                ('sex', models.CharField(blank=True, default='', max_length=10, null=True)),
                ('address', models.CharField(blank=True, default='', max_length=500, null=True)),
                ('mobile', models.BigIntegerField(blank=True, default=0, null=True)),
                ('aadhar_no', models.CharField(blank=True, default='', max_length=12, null=True, unique=True)),
                ('email_id', models.EmailField(blank=True, default='', max_length=254, null=True)),
            ],
        ),
    ]
