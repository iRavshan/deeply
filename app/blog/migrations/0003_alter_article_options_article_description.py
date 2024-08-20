# Generated by Django 5.0.8 on 2024-08-20 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['-created_at']},
        ),
        migrations.AddField(
            model_name='article',
            name='description',
            field=models.TextField(null=True, verbose_name='description'),
        ),
    ]
