# Generated by Django 3.2.21 on 2023-10-04 11:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0003_auto_20231004_1138'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='activity_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='classes.activitytype'),
        ),
    ]