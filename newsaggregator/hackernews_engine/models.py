from django.db import models

# Create your models here.

class Items (models.Model):
    """Create Items model and specify database Columns"""
    type = models.CharField(max_length=15,null=True)
    title = models.CharField(max_length=200,null=True)
    time = models.DateTimeField(blank=True,null=True)
    id = models.IntegerField(primary_key=True)
    score = models.IntegerField(blank=True,null=True)

    def __str__(self):
        return "{}".format((self.id,self.type,self.title
        ,self.score))
  




