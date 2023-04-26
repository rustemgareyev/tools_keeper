from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Tool(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name = 'tools')

    class Meta:
        ordering = ['-name']
        verbose_name = 'Оборудование'
        verbose_name_plural = 'Оборудование'

    def __str__(self):
        return self.name
