from django.db import models


class Tag(models.Model):
    name = models.CharField(
        max_length=255,
        unique=True,
        blank=False,
        null=False
    )

    def __str__(self):
        return self.name


class Task(models.Model):
    content = models.TextField(blank=False, null=False)
    datetime = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(null=True, blank=True)
    is_done = models.BooleanField(default=False)
    tags = models.ManyToManyField(
        Tag,
        blank=False,
        null=False,
        related_name='tasks',
    )

    @property
    def is_finished(self):
        return "Done" if self.is_done else "Not Done"

    def __str__(self):
        return f"{self.content} ({self.is_finished})"
