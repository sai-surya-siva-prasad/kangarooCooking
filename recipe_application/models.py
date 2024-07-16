from django.db import models

class Recipe(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    cooking_time = models.IntegerField(help_text="Cooking time in minutes")
    country = models.CharField(max_length=100)
    ingredients = models.JSONField()  # Store as a JSON array of objects
    instructions = models.JSONField()  # Store as a JSON array of objects
    image = models.ImageField(upload_to='recipes/images/', null=True, blank=True)
    video = models.FileField(upload_to='recipes/videos/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']