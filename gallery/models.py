from django.db import models
from category.models import category
from django.contrib.auth.models import User
from album.storage_backend import MediaStorage

class Gallery(models.Model):
    category_id = models.ForeignKey(category, on_delete=models.DO_NOTHING)
    user_id = models.ForeignKey(User,on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    upload = models.FileField(storage=MediaStorage())

    def __str__(self):
        return self.title
    
