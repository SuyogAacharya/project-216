# Generated by Django 5.0.1 on 2024-02-06 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_delete_courseitem'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='marks',
            field=models.IntegerField(default=1),
        ),
    ]
