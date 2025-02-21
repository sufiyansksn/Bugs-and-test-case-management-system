# Generated by Django 3.2.5 on 2021-10-30 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('managementapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('manager_email', models.CharField(max_length=100)),
                ('status', models.CharField(max_length=100)),
                ('employee_email', models.EmailField(max_length=254)),
                ('project', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
                ('enddate', models.DateField()),
            ],
        ),
    ]
