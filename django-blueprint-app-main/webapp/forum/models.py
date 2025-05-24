# forum/models.py
from django.contrib.auth.models import User
from django.db import models

class KoloMembership(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    kolo = models.CharField(max_length=10)  # e.g. 'kolo-1'

    class Meta:
        unique_together = ('user', 'kolo')

    def __str__(self):
        return f"{self.user.username} ∈ {self.kolo}"

class ForumPost(models.Model):
    author     = models.ForeignKey(User, on_delete=models.CASCADE)
    kolo       = models.CharField(max_length=10)  # e.g. 'kolo-2'
    content    = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"[{self.kolo}] {self.author.username}: {self.content[:20]}…"
