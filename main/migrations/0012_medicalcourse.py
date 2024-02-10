# Generated by Django 5.0.1 on 2024-02-10 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_questionbankcourse_remove_qbankscoreboard_course_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='MedicalCourse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='course_images/')),
                ('duration_months', models.IntegerField()),
                ('seats_available', models.IntegerField()),
                ('team_members', models.IntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
            ],
        ),
    ]
