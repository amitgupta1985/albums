from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import category


class categorySerialiazer(serializers.ModelSerializer):

    name = serializers.CharField(
            max_length=100,
            required=True,
            validators=[UniqueValidator(queryset=category.objects.all())]
        )
    class Meta:
        model = category
        fields = '__all__'