# Generated by Django 4.1.7 on 2023-04-05 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('titanic', '0002_alter_data_sex'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='predictions',
            field=models.PositiveIntegerField(blank=True, max_length=100),
        ),
    ]
