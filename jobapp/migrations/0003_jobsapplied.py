# Generated by Django 3.1.7 on 2021-04-22 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobapp', '0002_auto_20210420_1453'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobsApplied',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('job_id', models.IntegerField()),
                ('job_cat', models.CharField(max_length=10)),
            ],
        ),
    ]