# Generated by Django 5.1 on 2024-08-13 04:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0006_alter_course_id_alter_course_level_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='order',
            field=models.PositiveSmallIntegerField(blank=True, editable=False),
        ),
    ]
