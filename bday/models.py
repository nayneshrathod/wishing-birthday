from django.db import models

from django.template.defaultfilters import slugify  # new
from django.urls import reverse


class wish(models.Model):
    toname = models.CharField(max_length=120, verbose_name='Birthday person')
    fromname = models.CharField(max_length=120, verbose_name='wish Sender person')
    slug = models.SlugField()
    wishurl = models.URLField(max_length=300)

    def __str__(self):
        return self.slug
        # return "%s wish to %s" % (self.fromname, self.toname)

    def get_absolute_url(self):
        return reverse('wishto', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):  # new
        if not self.slug:
            s = self.toname + " " + self.fromname
            self.slug = slugify(s, )

        if not self.wishurl:
            self.wishurl = "http://127.0.0.1:8000/%s" % self.slug
            # self.wishurl

        return super().save(*args, **kwargs)
    #
    #
    #
    # def save(self):
    #     if not self.id:
    #         self.s = slugify(self.q)
    #
    #     super(Test, self).save()
