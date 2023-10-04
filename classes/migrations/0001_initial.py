# Generated by Django 3.2.21 on 2023-10-03 16:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ActivityType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
                ('description', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
                ('description', models.TextField()),
                ('date', models.DateTimeField()),
                ('locaton', models.CharField(max_length=200)),
                ('max_participants', models.PositiveIntegerField(default=10)),
                ('current_participants', models.PositiveIntegerField(default=0)),
                ('activity_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='classes.activitytype')),
            ],
            options={
                'verbose_name': 'Activity',
                'verbose_name_plural': 'Activities',
                'ordering': ['date'],
            },
        ),
    ]
