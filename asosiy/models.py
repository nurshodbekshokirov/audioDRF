from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
import os

class Topic(models.Model):
    nom = models.CharField(max_length=300)

    def __str__(self):
        return self.nom

def validate_mp3(value):
    ext = os.path.splitext(value.name)[1]
    valid_extensions = ['.mp3']
    if not ext.lower() in valid_extensions:
        raise ValidationError(_('Faqat .mp3 fayllar qabul qilinadi'), code='invalid')


class Audio(models.Model):
    name = models.CharField(max_length=300)
    location = models.FileField(validators=[validate_mp3])
    duration = models.DurationField()
    size = models.PositiveSmallIntegerField()
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

# Create your models here.
