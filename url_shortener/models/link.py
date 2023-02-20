from django.db import models
from django.utils.crypto import get_random_string


class LinkModel(models.Model):
    link_key = models.CharField(max_length=50, unique=True)
    link = models.TextField()

    def save(self, *args, **kwargs):
        while True:
            link_key = get_random_string(length=5).lower()
            try:
                LinkModel.objects.get(link_key=link_key)
            except LinkModel.DoesNotExist:
                self.link_key = link_key
                break
        super(LinkModel, self).save(*args, **kwargs)
