from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from .models import Gallery
from .serializers import GallerySerializers
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404;
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


class GalleyAPIView(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = [IsAuthenticated]
    def get(self, request):
        gallery = Gallery.objects.filter(user_id=request.user)
        serializer = GallerySerializers(gallery, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        gallery = request.data
        serializer = GallerySerializers(data=gallery)
        if serializer.is_valid():
            serializer.save(user_id=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class GalleryDetailView(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = [IsAuthenticated]
    def get_object(self, id):
        try:
            return Gallery.objects.get(id=id)
        except Gallery.DoesNotExist as e:
            raise Http404

    def get(self, request, id=None):
        gallerData = self.get_object(id)
        serializer = GallerySerializers(gallerData)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, id=None):
        galleryData = self.get_object(id)
        gallery = request.data
        serializer = GallerySerializers(galleryData, data=gallery)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id=None):
        gallerData = self.get_object(id)
        gallerData.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def gallerylist(request):
    gallerData = Gallery.objects.all()
    serializer = GallerySerializers(gallerData, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK) 

@api_view(['GET'])
def detail(request,id):    
    try:
        gallerData = Gallery.objects.get(id=id)
        serializer = GallerySerializers(gallerData)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Gallery.DoesNotExist as e:
        return Response({"error":"Gallery data not exist"},status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def getByCategory(request,category_id):
    galleryData = Gallery.objects.filter(category_id=category_id)
    if galleryData:
        serializer = GallerySerializers(galleryData, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response({"error":"No data found"},status=status.HTTP_404_NOT_FOUND)        


    

