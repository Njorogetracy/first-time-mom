# Generated by Django 3.2.21 on 2023-10-23 14:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0009_alter_review_activity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='activity',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classes.activity'),
        ),
    ]
