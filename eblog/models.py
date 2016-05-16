from django.db import models
from django.core.urlresolvers import reverse
from django.utils.encoding import python_2_unicode_compatible


from django.contrib.contenttypes.fields import GenericRelation
from hitcount.models import HitCount, HitCountMixin


class EntryQuerySet(models.QuerySet):
    def published(self):
        return self.filter(publish=True)

class Tag(models.Model):
    slug = models.SlugField(max_length=200, unique=True)

    def __str__(self):
        return self.slug

@python_2_unicode_compatible
class Entry(models.Model, HitCountMixin):
    title = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='static/images/%Y/%m/%d', null=True)
    headerline = models.TextField(max_length=100, default="Header Line")
    header_desc = models.TextField(max_length=200, default="Short description")
    tags = models.ManyToManyField(Tag)
    body = models.TextField()
    slug = models.SlugField(max_length=200, unique=True)
    publish = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    hit_count_generic = GenericRelation(
        HitCount, object_id_field='object_pk',
        related_query_name='hit_count_generic_relation')

    objects = EntryQuerySet.as_manager()

    def get_absolute_url(self):
      return reverse("entry_detail", kwargs={"slug": self.slug})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Blog Entry"
        verbose_name_plural = "Blog Entries"
        ordering = ["-created"]
