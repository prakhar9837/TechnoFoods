# Generated by Django 2.2.7 on 2019-11-26 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customerapp', '0004_auto_20191115_1756'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerclass',
            name='id',
            field=models.CharField(max_length=20, primary_key=True, serialize=False),
        ),
    ]
