from django.conf import settings
from django.db import models


class Message(models.Model):
    PREVIEW_LENGTH = 50

    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    tags = models.ManyToManyField("Tag", blank=True)
    image = models.ImageField(upload_to='messages/', null=True, blank=True)
    liked_by = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name='liked_messages',
        blank=True
    )

    def __str__(self):
        return self.text

    @property
    def text_preview(self):
        if len(self.text) <= self.PREVIEW_LENGTH:
            return self.text

        return self.text[:self.PREVIEW_LENGTH] + '...'


class Tag(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name
