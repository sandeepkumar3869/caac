# Generated by Django 4.2.7 on 2023-12-01 08:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bottomlevel', '0002_alter_bottomlevel_task_ccompleted_on_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bottomlevel',
            name='task_created_on',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 1, 14, 27, 30, 457629)),
        ),
    ]
