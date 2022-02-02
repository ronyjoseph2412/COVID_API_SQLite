from django.shortcuts import render

# Create your views here.
import json
from django.shortcuts import render
# For Allowing the users to use the API Methods
from django.views.decorators.csrf import csrf_exempt 
# Parser to parse the incoming data to data_model
from rest_framework.parsers import JSONParser
# 
from django.http.response import JsonResponse
# Create your views here.

from COVID.models import COVID_India
from COVID.serializers import COVID_India_Serializer

@csrf_exempt
def COVID_India_request(request,id='India'):
    if(request.method=='GET'):
        COVID_data=COVID_India.objects.all()
        covid_serializer=COVID_India_Serializer(COVID_data,many=True)
        return JsonResponse(covid_serializer.data,safe=False)
    elif(request.method=='POST'):
        covid_data=JSONParser().parse(request)
        covid_serializer=COVID_India_Serializer(data=covid_data)
        # print(covid_serializer)
        if(covid_serializer.is_valid()):
            covid_serializer.save()
            return JsonResponse("Posted Successfully!",safe=False)
        return JsonResponse("Failed to Post!Please try later!")
    elif(request.method=='PUT'):
        covid_data=JSONParser().parse(request)
        # print(covid_data)
        covid=COVID_India.objects.get(Region=covid_data['Region'])
        covid_serializer=COVID_India_Serializer(covid,data=covid_data)
        # print(covid_serializer)
        if(covid_serializer.is_valid()):
            covid_serializer.save()
            return JsonResponse("Update Successful!",safe=False)
        return JsonResponse("Failed tp update!Please try again!")
    elif(request.method=='DELETE'):
        covid=COVID_India.objects.get(Region=id)
        covid.delete()
        return JsonResponse("Deleted Successfully",safe=False)