from django.db import models
import re


class Customer(models.Model):
    added_at = models.DateTimeField(auto_now_add=True)
    last_edit = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=255, unique=True)

    def save(self, *args, **kwargs) -> None:
        pattern = re.compile(r"\s{2,}")
        saved_name = pattern.sub(" ", self.name)
        self.name = " ".join(word.capitalize() for word in saved_name.split(" "))
        return super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.name
