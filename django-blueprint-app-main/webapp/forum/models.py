from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    KOLO_CHOICES = [
        ('kolo-1', 'Koło 1'),
        ('kolo-2', 'Koło 2'),
        ('kolo-3', 'Koło 3'),
        ('kolo-4', 'Koło 4'),
    ]
    kolo = models.CharField(max_length=10, choices=KOLO_CHOICES)
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} ({self.kolo})"