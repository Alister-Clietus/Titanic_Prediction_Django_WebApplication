# Generated by Django 4.1.7 on 2023-04-05 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('titanic', '0011_alter_data_predictions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='predictions',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
