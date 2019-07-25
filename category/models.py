from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

class category(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.DO_NOTHING,null=True)
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    updated_at = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.name
