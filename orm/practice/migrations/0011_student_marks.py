# Generated by Django 4.1.7 on 2023-03-20 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('practice', '0010_alter_brocamp_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='marks',
            field=models.IntegerField(default=0),
        ),
    ]
