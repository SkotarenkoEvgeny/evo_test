from django.db import models


class SimpleName(models.Model):
    name = models.CharField(
        max_length=200, unique=True
        )
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
