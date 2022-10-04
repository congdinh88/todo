from django.db import models


class TodoApp(models.Model):
    name = models.CharField(max_length=512, unique=True)
    complete = models.BooleanField(default=False)

    def __str__(self):
        return self.name
