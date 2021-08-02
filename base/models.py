from django.db import models

# Create your models here.
class Event(models.Model):
    eventTitle = models.TextField(null=False,blank=False)
    eventdesc = models.TextField(null=True,blank=True)
    eventDate = models.DateTimeField(null=True,blank=True)
    eventLocation = models.TextField(null=True,blank=True)
    # eventImg
def __str__(self):
    return self.eventTitle