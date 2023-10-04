# Generated by Django 3.2.21 on 2023-10-04 09:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='activitytype',
            name='description',
        ),
        migrations.RemoveField(
            model_name='activitytype',
            name='name',
        ),
        migrations.AddField(
            model_name='activitytype',
            name='type',
            field=models.CharField(choices=[('Course', 'Class'), ('Group Counseling', 'Group Counseling'), ('Yoga Session', 'Yoga Session')], default='Course', max_length=20),
        ),
        migrations.AlterField(
            model_name='activity',
            name='activity_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='classes.activitytype'),
        ),
    ]