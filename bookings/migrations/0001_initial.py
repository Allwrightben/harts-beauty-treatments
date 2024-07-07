# Generated by Django 4.2.13 on 2024-07-07 12:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=15)),
                ('treatment', models.IntegerField(choices=[(0, 'Botox Therapy(chronic pain relief)'), (1, 'Botox Treatment (wrinkle reduction/prevention)'), (2, 'CHemical Peel (skin rejuvenation)'), (3, 'Dermal Fillers (facce sculpting/wrinkle reduction)'), (4, 'Hyperhidrosis (excessive sweating treatment)'), (5, 'Lip filler (lip augmentation)'), (6, 'Skin: Hydrafacial'), (7, 'Skin: Profhilo Treatment'), (8, 'Wrinkle softening injections')])),
                ('date', models.DateField()),
                ('time', models.IntegerField(choices=[(0, '9:00-9:45'), (1, '10:00-10:45'), (2, '11:00-11:45'), (3, '14:00-14:45'), (4, '15:00-15:45'), (5, '16:00-16:45'), (6, '17:00-17:45'), (7, '18:00-18:45')])),
                ('message', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
