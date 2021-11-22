from datetime import datetime, timezone

from django.db import models

from users.models import User


class BaseModel(models.Model):
    class Meta:
        abstract = True

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Dog(BaseModel):
    SIZE_CHOICE = [
    ('Mały', 'Mały'),
    ('Średni', 'Średni'),
    ('Duży', 'Duży'),
]
    name = models.CharField(max_length=255, blank=False)
    age = models.PositiveSmallIntegerField()
    cage = models.PositiveSmallIntegerField()
    sheltered_at = models.DateField()
    size = models.CharField(
        max_length=6,
        choices=SIZE_CHOICE,
        default='Średni'
    )


class Comment(BaseModel):
    post = models.ForeignKey(
        Dog,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    body = models.TextField()

    class Meta:
        ordering = ('created_at',)

    def __str__(self) -> str:
        return f'Comment by {self.name} on {self.post}'


class File(BaseModel):
    file = models.FileField(blank=False, null=False)
    dog = models.ForeignKey(Dog, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'Dog: {dog.name} - self.file.name'