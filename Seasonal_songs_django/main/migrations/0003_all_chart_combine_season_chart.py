# Generated by Django 5.0.4 on 2024-04-18 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_spring_modal_chart_winter_modal_chart_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='All_chart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rank', models.IntegerField()),
                ('title', models.CharField(default='', max_length=100)),
                ('singer', models.CharField(default='', max_length=100)),
                ('years', models.CharField(default='', max_length=100)),
                ('date', models.DateField()),
                ('month', models.IntegerField()),
                ('day', models.IntegerField()),
                ('week', models.IntegerField()),
            ],
            options={
                'db_table': 'All_chart',
            },
        ),
        migrations.CreateModel(
            name='Combine_season_chart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=100)),
                ('singer', models.CharField(default='', max_length=100)),
                ('years', models.CharField(default='', max_length=100)),
            ],
            options={
                'db_table': 'Combine_season_chart',
            },
        ),
    ]
