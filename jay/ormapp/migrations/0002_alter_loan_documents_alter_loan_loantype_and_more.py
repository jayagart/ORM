# Generated by Django 5.1.2 on 2024-10-22 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ormapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loan',
            name='documents',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='loan',
            name='loantype',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='loan',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]