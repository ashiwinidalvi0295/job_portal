# Generated by Django 3.1.7 on 2021-04-20 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CivilJobs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=50)),
                ('job_profile', models.CharField(max_length=50)),
                ('job_discription', models.CharField(max_length=100)),
                ('job_requirements', models.CharField(max_length=100)),
                ('experience', models.FloatField()),
                ('package', models.FloatField()),
                ('no_of_vaccancy', models.IntegerField()),
                ('location', models.CharField(max_length=50)),
                ('Mod_date', models.DateField()),
                ('last_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='ITJobs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=50)),
                ('job_profile', models.CharField(max_length=50)),
                ('job_discription', models.CharField(max_length=100)),
                ('job_requirements', models.CharField(max_length=100)),
                ('experience', models.FloatField()),
                ('package', models.FloatField()),
                ('no_of_vaccancy', models.IntegerField()),
                ('location', models.CharField(max_length=50)),
                ('Mod_date', models.DateField()),
                ('last_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='MechJobs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=50)),
                ('job_profile', models.CharField(max_length=50)),
                ('job_discription', models.CharField(max_length=100)),
                ('job_requirements', models.CharField(max_length=100)),
                ('experience', models.FloatField()),
                ('package', models.FloatField()),
                ('no_of_vaccancy', models.IntegerField()),
                ('location', models.CharField(max_length=50)),
                ('Mod_date', models.DateField()),
                ('last_date', models.DateField()),
            ],
        ),
        migrations.DeleteModel(
            name='Civil_Jobs',
        ),
        migrations.DeleteModel(
            name='IT_Jobs',
        ),
        migrations.DeleteModel(
            name='Mech_Jobs',
        ),
    ]
