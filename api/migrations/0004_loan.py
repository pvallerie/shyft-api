# Generated by Django 3.0 on 2021-02-17 19:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_bike_rate'),
    ]

    operations = [
        migrations.CreateModel(
            name='Loan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pickup_date', models.DateField()),
                ('dropoff_date', models.DateField()),
                ('bike', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Bike')),
                ('bike_loaner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='loans', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
