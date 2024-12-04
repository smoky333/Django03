from django.db import models
from django.contrib.auth.models import User  # Для связи с зарегистрированным пользователем

class News(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # Связь с моделью пользователя

    def __str__(self):
        return self.title
