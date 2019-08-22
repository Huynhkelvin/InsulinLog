# Generated by Django 2.2.3 on 2019-08-04 20:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='DailyInsulin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meal_time', models.DateTimeField(blank=True)),
                ('meal', models.CharField(blank=True, choices=[('No meal', 'No Meal'), ('Breakfast', 'Breakfast'), ('Lunch', 'Lunch'), ('Dinner', 'Dinner'), ('Bedtime', 'Bedtime'), ('Snack', 'Snack')], max_length=10)),
                ('curr_BSL', models.IntegerField(blank=True)),
                ('diff_BSL', models.IntegerField(blank=True)),
                ('correction_insulin', models.IntegerField(blank=True)),
                ('total_carb', models.IntegerField(blank=True)),
                ('carb_ratio', models.IntegerField(blank=True)),
                ('insulin_dose', models.IntegerField(blank=True)),
                ('total_insulin', models.IntegerField(blank=True)),
                ('notes', models.TextField(blank=True)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
