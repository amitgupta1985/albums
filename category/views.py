from django.shortcuts import render

from django.http import HttpResponse, JsonResponse
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import JSONParser
from .models import category
from .serializers import categorySerialiazer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import authentication_classes,permission_classes,api_view
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated,IsAdminUser


@api_view(['GET','POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated,IsAdminUser])
def categ(request):
    if request.method == "GET":
        categList = category.objects.all()
        serializer = categorySerialiazer(categList, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == "POST":
        json_parser = JSONParser()
        categData = json_parser.parse(request)
        categData['user_id'] = request.user.id
        serializer = categorySerialiazer(data=categData)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        else:    
            return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def catedetails(request, id):
    try:
        catInstance = category.objects.get(id=id)
    except category.DoesNotExist as e:
        return JsonResponse({"error": "No data found" }, status=status.HTTP_404_NOT_FOUND)
    if request.method == "GET":
        serializer = categorySerialiazer(catInstance)
        return JsonResponse(serializer.data)
    elif request.method == "PUT":
        json_parser = JSONParser()
        categData = json_parser.parse(request)
        serializer = categorySerialiazer(catInstance, data=categData)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_200_OK)
        else:    
            return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        catInstance.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def categList(request):
    categList = category.objects.all()
    serializer = categorySerialiazer(categList, many=True)
    return JsonResponse(serializer.data, safe=False)                
  