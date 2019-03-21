# Generated by Django 2.1.5 on 2019-03-18 07:09

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('course_code', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('course_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Lecturer',
            fields=[
                ('staff_no', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('full_name', models.CharField(max_length=200)),
                ('lec_units', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200), blank=True, null=True, size=None)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('adm_no', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('full_name', models.CharField(max_length=200)),
                ('units', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200), blank=True, null=True, size=None)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='assignment.Course')),
            ],
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('unit_code', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('unit_name', models.CharField(max_length=100)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='assignment.Course')),
            ],
        ),
    ]
