# Generated by Django 4.2.13 on 2024-07-04 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('treatments', '0002_treatment_excerpt'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='treatment',
            options={'ordering': ['title']},
        ),
        migrations.AlterField(
            model_name='treatment',
            name='price',
            field=models.IntegerField(),
        ),
    ]
