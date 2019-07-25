from rest_framework import serializers
from .models import Gallery
from category.models import category


class GallerySerializers(serializers.ModelSerializer):    

    class Meta:
        model = Gallery        
        fields = ('id','category_id','title','description','uploaded_at','upload')