# Generated by Django 3.0.5 on 2020-11-28 22:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('address', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('food_genre', models.CharField(max_length=100)),
                ('price_range', models.CharField(choices=[('$', 'One'), ('$$', 'Two'), ('$$$', 'Three'), ('$$$$', 'Four')], max_length=4)),
                ('rating', models.DecimalField(decimal_places=1, max_digits=2)),
                ('open_time', models.TimeField()),
                ('close_time', models.TimeField()),
                ('address', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='address.Address')),
            ],
        ),
    ]
