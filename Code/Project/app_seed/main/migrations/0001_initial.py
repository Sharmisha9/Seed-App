# Generated by Django 4.1.1 on 2022-09-25 02:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('phone', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street', models.CharField(max_length=1024, verbose_name='street')),
                ('city', models.CharField(max_length=100, verbose_name='city')),
                ('state', models.CharField(max_length=3, verbose_name='state')),
                ('zip', models.CharField(max_length=6, verbose_name='zip')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.users')),
            ],
            options={
                'ordering': ['zip'],
            },
        ),
    ]
