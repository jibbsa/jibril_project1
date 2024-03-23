from django.db import models

class Artist(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Category(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title

class Painting(models.Model):
    name = models.CharField(max_length=100)
    artist = models.ForeignKey(Artist, on_delete=models.SET_NULL, null=True, related_name='paintings')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='paintings')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True)
    available = models.BooleanField(default=True)

    def __str__(self):
        artist_name = self.artist.name if self.artist else 'Unknown Artist'
        return f"{self.name} by {artist_name}"
