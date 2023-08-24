# Generated by Django 4.1.1 on 2022-10-24 06:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_crop_season_soil_delete_address_delete_users_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CropAdv',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('max_temp', models.FloatField()),
                ('min_temp', models.FloatField()),
                ('max_humidity', models.FloatField()),
                ('min_humidity', models.FloatField()),
                ('max_pH', models.FloatField()),
                ('min_pH', models.FloatField()),
                ('season', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.season')),
                ('soil', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.soil')),
            ],
        ),
    ]