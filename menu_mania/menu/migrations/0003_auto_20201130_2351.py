# Generated by Django 3.0.5 on 2020-11-30 23:51

from django.db import migrations, models
import django_mysql.models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0002_auto_20201130_0725'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dish',
            name='allergens',
            field=django_mysql.models.ListCharField(models.CharField(max_length=12), max_length=130, null=True, size=10),
        ),
    ]
