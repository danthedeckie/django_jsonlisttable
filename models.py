from collections import namedtuple
from django.db import models
import jsonlistedit

TableField = namedtuple('TableField', ['name', 'title'])

ORDERLIST_CONFIG = {
    "debug": False,
    "fields": [TableField(*v) for v in (
        ('name', "Name"),
        ('price', "Price"),
        ('quantity', 'Quantity'))],
    "allow_titles": True,
    "allow_notes": True,
}

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    status = models.IntegerField(default=1)

class Order(models.Model):
    title = models.CharField(max_length=100)
    orderlist = jsonlistedit.JSONListEditField(template="orderlist_widget.html", config=ORDERLIST_CONFIG)
