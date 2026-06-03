from django.db import models


class Game(models.Model):
    title = models.CharField(max_length=225, unique=True)
    slug = models.SlugField(max_length=225, unique=True)
    logo = models.ImageField(upload_to='game_logos/', null=True, blank=True)
    def __str__(self):
        return self.title
    
    
class Category(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    title = models.CharField(max_length=225)
    slug = models.SlugField(max_length=225)
    def __str__(self):
        return f"{self.game.title} - {self.title}"
