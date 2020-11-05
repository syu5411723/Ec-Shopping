from django.db import models


class Post(models.Model):
    name = models.CharField(max_length=150)
    price = models.IntegerField()
    content = models.TextField(max_length=500, null=True)
    thumbnail = models.ImageField(upload_to='thumbnails/')

    def __str__(self):
        return self.name
