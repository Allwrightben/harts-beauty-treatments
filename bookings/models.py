from django.db import models
from django.contrib.auth.models import User

# Time slots
TIME_SLOTS = (
    (0, '9:00-9:45'),
    (1, '10:00-10:45'),
    (2, '11:00-11:45'),
    (3, '14:00-14:45'),
    (4, '15:00-15:45'),
    (5, '16:00-16:45'),
    (6, '17:00-17:45'),
    (7, '18:00-18:45'),
)

TREATMENTS = (
    (-1, 'Select a treatment'),
    (0, 'Botox Therapy(chronic pain relief)'),
    (1, 'Botox Treatment (wrinkle reduction/prevention)'),
    (2, 'Chemical Peel (skin rejuvenation)'),
    (3, 'Dermal Fillers (facce sculpting/wrinkle reduction)'),
    (4, 'Hyperhidrosis (excessive sweating treatment)'),
    (5, 'Lip filler (lip augmentation)'),
    (6, 'Skin: Hydrafacial'),
    (7, 'Skin: Profhilo Treatment'),
    (8, 'Wrinkle softening injections'),
)

# Booking model
class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, default="Your Name")
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    treatment = models.IntegerField(choices=TREATMENTS)
    date = models.DateField()
    time = models.IntegerField(choices=TIME_SLOTS)
    message = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} - {self.date} - {self.get_time_display()}"
