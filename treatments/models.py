from django.db import models
from django.contrib.auth.models import User


'''
status options as choices for treatments so
site owner can choose to publish or keep as draft
'''
STATUS = ((0, "Draft"), (1, "Published"))


# Treatment model which will map to a database table
class Treatment(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    content = models.TextField()
    excerpt = models.TextField(blank=True)
    price = models.IntegerField()
    status = models.IntegerField(choices=STATUS, default=0)

    def __str__(self):
        return f"Treatment: {self.title}"
    class Meta:
        ordering = ['title']

