# Generated by Django 2.2 on 2019-04-20 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_auto_20190417_1258'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='total_cost',
            field=models.DecimalField(decimal_places=2, default=22, max_digits=15),
        ),
    ]
