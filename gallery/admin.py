from django.contrib import admin
from .models import Gallery

class GalleryAdmin(admin.ModelAdmin):
    list_display = ('id','title','uploaded_at')

admin.site.register(Gallery, GalleryAdmin)
