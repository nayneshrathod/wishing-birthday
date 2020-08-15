from django.db import models

from django.template.defaultfilters import slugify  # new
from django.urls import reverse


class wish(models.Model):
    toname = models.CharField(max_length=120)
    fromname = models.CharField(max_length=120)
    slug = models.SlugField()

    def __str__(self):
        return "%s wish to %s" % (self.fromname) (self.toname)

    def get_absolute_url(self):

        return reverse('article_detail', kwargs={'slug': self.__str__()})

    def save(self, *args, **kwargs):  # new
        if not self.slug:
            self.slug = slugify(self.toname)
        return super().save(*args, **kwargs)
