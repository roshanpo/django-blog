from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length = 100)
    content = models.TextField()
    time_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete = models.CASCADE)#basically telling django to delete the post if the user gets deleted
    #basically foreignkey is using other models. Here, we are using model User from users/models.
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs ={'pk' : self.pk})
