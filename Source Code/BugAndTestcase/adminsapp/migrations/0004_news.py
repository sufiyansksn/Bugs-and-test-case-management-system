# Generated by Django 3.2.5 on 2021-11-06 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminsapp', '0003_project'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
                ('date', models.DateField()),
            ],
        ),
    ]
