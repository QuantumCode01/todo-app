# Generated by Django 4.1.4 on 2023-06-30 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_alter_task_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='title',
            field=models.CharField(max_length=250, unique=True),
        ),
    ]
