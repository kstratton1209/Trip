# Generated by Django 2.2.4 on 2020-08-06 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trips',
            name='end_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='trips',
            name='start_date',
            field=models.DateField(),
        ),
    ]