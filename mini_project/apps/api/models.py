from django.db import models
from apps.authentication.models import User


class Word(models.Model):
    name = models.CharField(max_length=100)
    #this gives a db attached to this user
    owner = models.ForeignKey(User, on_delete= models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)#time stampe when this was created
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Definition(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    word = models.ForeignKey(Word, related_name='definitions', on_delete=models.CASCADE)
    definition = models.TextField(blank=True)
    part_of_speech= models.TextField(blank=True)
    sentence = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)  # time stampe when this was created
    updated_at = models.DateTimeField(auto_now=True)
    is_public = models.BooleanField(default=True)

    #we are not going to see it this way.. this is just created the instances we want to input
    #and building the realaitonship between the two classes