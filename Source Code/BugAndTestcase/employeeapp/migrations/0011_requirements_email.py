# Generated by Django 3.2.12 on 2024-05-24 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employeeapp', '0010_requirements'),
    ]

    operations = [
        migrations.AddField(
            model_name='requirements',
            name='email',
            field=models.EmailField(default=1, max_length=254),
            preserve_default=False,
        ),
    ]
