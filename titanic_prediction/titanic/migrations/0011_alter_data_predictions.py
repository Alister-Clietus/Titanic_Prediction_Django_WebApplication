# Generated by Django 4.1.7 on 2023-04-05 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('titanic', '0010_alter_data_predictions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='predictions',
            field=models.PositiveIntegerField(blank='True'),
        ),
    ]