from django.db import models


class TestModel(models.Model):
    field1 = models.CharField(max_length=100)
    field2 = models.IntegerField(default=1)
    field3 = models.SlugField()
