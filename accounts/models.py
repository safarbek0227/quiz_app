from email.policy import default
from django.db import models
from django.conf import settings
from main.models import Test
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=None, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='users/', blank=True, default='/images/alert.png')
    rank = models.ManyToManyField(Test)
    is_permissions = models/
    short_info = models.TextField(max_length=200, blank=True)


    def image_url(self):
        if self.photo:
            return getattr(self.photo, 'url', "/static/img/nouser.png")
        return None


    def __str__(self):
        return 'Profile for user {}'.format(self.user.username)
