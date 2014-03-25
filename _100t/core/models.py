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
    title = models.CharField(max_length=256)
    owner = models.ForeignKey(User, verbose_name="List owner")
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('id', 'owner')
        ordering = ('created', )

    def __unicode__(self):
        return self.name

class Item(models.Model):
    short_name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    is_set = models.BooleanField("item is a set of sub-items", default=False)
    sub_index = models.PositiveIntegerField(default=0) #index in the sub-item list if this is a sub item
    own_date = models.DateField(blank=True, null=True)
    parent_item = models.ForeignKey("self", verbose_name="item's parent item", blank=True, null=True)

    def __unicode__(self):
        return self.short_name

class ListItem(models.Model):
    item_list = models.ForeignKey(List)
    item = models.ForeignKey(Item)
    item_category = models.ManyToManyField(Category)
    item_index = models.PositiveIntegerField()

    def __unicode__(self):
        return "%d - %d" % (item_list, item_index)

    class Meta:
        unique_together = ('item_list', 'item', 'item_index')
