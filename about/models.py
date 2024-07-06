from django.db import models


class About(models.Model):
    title = models.CharField(max_length=200)
    name = models.CharField(max_length=100, default="Your Name") 
    professional = models.CharField()
    personal = models.CharField()
    updated_on = models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return self.title