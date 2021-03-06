# Generated by Django 3.1.3 on 2020-11-23 21:59

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schema', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='schemacolumns',
            name='column_name',
            field=models.TextField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='schemacolumns',
            name='address',
            field=models.CharField(help_text='Address', max_length=150, verbose_name='Address'),
        ),
        migrations.AlterField(
            model_name='schemacolumns',
            name='company_name',
            field=models.CharField(help_text='Company', max_length=100, verbose_name='Company'),
        ),
        migrations.AlterField(
            model_name='schemacolumns',
            name='first_name',
            field=models.TextField(help_text='Name', max_length=50, verbose_name='First name'),
        ),
        migrations.AlterField(
            model_name='schemacolumns',
            name='integer',
            field=models.IntegerField(default=18, validators=[django.core.validators.MaxValueValidator(60), django.core.validators.MinValueValidator(18)]),
        ),
        migrations.AlterField(
            model_name='schemacolumns',
            name='job',
            field=models.CharField(help_text='Job role', max_length=50, verbose_name='Job'),
        ),
        migrations.AlterField(
            model_name='schemacolumns',
            name='last_name',
            field=models.TextField(help_text='Name', max_length=50, verbose_name='Last name'),
        ),
    ]
