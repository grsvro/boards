# Generated by Django 5.1.5 on 2025-01-29 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_alter_task_date_alter_task_menu'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='weight',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='task',
            name='age',
            field=models.IntegerField(default=0),
        ),
    ]
