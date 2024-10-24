# Generated by Django 5.1.2 on 2024-10-22 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Loan',
            fields=[
                ('lid', models.CharField(max_length=15, primary_key='lid', serialize=False)),
                ('loantype', models.CharField(max_length=3)),
                ('name', models.CharField(max_length=7)),
                ('age', models.IntegerField()),
                ('aadhar', models.IntegerField()),
                ('documents', models.CharField(max_length=4)),
            ],
        ),
    ]
