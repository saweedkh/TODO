from django.db import models

from accounts.models import CustomUser

# Create your models here.


class TodoModel(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=225)
    text = models.TextField(blank=True)
    status = models.BooleanField(default=False)
    time = models.DateField(blank=True, null=True)

    datetime_created = models.DateTimeField(auto_now=True)
    datetime_modified = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'{self.user.username}: {self.title}'