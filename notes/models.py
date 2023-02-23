from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


class Profile(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=50)
    birth_date = models.DateField(null=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_profile')


# Create your models here.

class Notes(models.Model):
    TOPIC_TYPES = [
        (1, 'Важные срочные'),
        (2, 'Важные не срочные'),
        (3, 'Неважные срочные'),
        (4, 'Неважные не срочные'),
    ]
    title = models.CharField(max_length=50)
    text = models.TextField(max_length=1500)
    reminder = models.DateTimeField(null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author')
    type = models.IntegerField(choices=TOPIC_TYPES)

    class Meta:
        verbose_name = _("Notes")
        verbose_name_plural = _("Notes")

