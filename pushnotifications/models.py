from django.db import models

# Create your models here.
# notifications/models.py
from django.db import models
from accounts.models import AccountModel

class ExpoPushToken(models.Model):
    user = models.ForeignKey(AccountModel, on_delete=models.CASCADE, related_name='expo_push_tokens')
    token = models.CharField(max_length=255)

    def __str__(self):
        return self.token
