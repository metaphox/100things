from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)
    owner = models.ForeignKey(User, verbose_name="Category owner")

    class Meta:
        unique_together = ('id', 'owner')

    def __unicode__(self):
        return self.name

class List(models.Model):
    name = models.CharField(max_length=256)
    owner = models.ForeignKey(User, verbose_name="List owner")

    class Meta:
        unique_together = (('id', 'owner'), )

    def __unicode__(self):
        return self.name


class Item(models.Model):
    index = models.IntegerField()
    sub_index = models.IntegerField(null=True)
    short_name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    is_set = models.BooleanField("item is a set of sub-items", default=False)
    own_date = models.DateField(blank=True, null=True)
    parent_item = models.ForeignKey("self", verbose_name="item's parent item", blank=True, null=True)
    category = models.ManyToManyField(Category)
    item_list = models.ForeignKey(List)

    class Meta:
        unique_together = (('index', 'sub_index', 'item_list'), )

    def __unicode__(self):
        return self.short_name
