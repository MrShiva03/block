from django.db import models

class Article(models.Model):
    author = models.ForeignKey('auth.user', on_delete=models.CASCADE)
    title = models.CharField(max_length = 150)
    content = models.TextField()
    image = models.ImageField(upload_to="article/")
    created_at = models.DateField(auto_now_add=True)
