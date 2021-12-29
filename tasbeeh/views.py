from django.shortcuts import render
from tasbeeh.models import Zekr

from tasbeeh.serializers import ZekrSerializer, PostZekrSerializer, UpdateZekrSerializer, IncrementCounterSerializer ,DeleteZekrSerializer
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser
from rest_framework.response import Response

from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
 
# Create your views here.



@api_view(('GET',))
@renderer_classes((TemplateHTMLRenderer, JSONRenderer))
def get_first_zekr(request):
    queryset_dict = {}
    tutorial_data = Zekr.objects.get(pk=1)
    queryset_dict["id"] = tutorial_data.id
    queryset_dict["name"] = tutorial_data.name
    queryset_dict["counter"] = tutorial_data.counter
    serializer = ZekrSerializer(data=queryset_dict)   
    if serializer.is_valid():
        print("valid")
    else:
        print(serializer.errors)
    return Response(serializer.data)
 

@api_view(('GET',))
@renderer_classes((TemplateHTMLRenderer, JSONRenderer))
def get_all_zekr(request):
    tutorial_data = Zekr.objects.all()
    serializer = ZekrSerializer(data=tutorial_data, many=True)
    if serializer.is_valid():
        print("valid")
        #create_loan_service(serializer.validated_data,request)
        #serializer.save(user=request.user)
    else:
        print(serializer.errors)
    return Response(serializer.data)


@api_view(['POST'])
def post_new_zekr(request):
    print("POSTING ZEKR")
    tutorial_data = JSONParser().parse(request)
    serializer = PostZekrSerializer(data=tutorial_data)
    if serializer.is_valid():
        data = serializer.validated_data
        print(data)
        zekr = Zekr.objects.create(name = data['name'])
    else:
        print("THE ERRORS: ")
        print(serializer.errors)
    return Response(serializer.data)


@api_view(['POST'])
def delete_zekr(request):
    tutorial_data = JSONParser().parse(request)
    serializer = DeleteZekrSerializer(data=tutorial_data)
    if serializer.is_valid():
        data = serializer.validated_data
        print("DATAAA")
        print(data)
        zekr = Zekr.objects.get(pk=data['id'])
        zekr.delete()
       
    return Response(serializer.data)


@api_view(['POST'])
def update_zekr(request):
    print("Hello from update verse")
    tutorial_data = JSONParser().parse(request)
    serializer = UpdateZekrSerializer(data=tutorial_data)
    if serializer.is_valid():
        data = serializer.validated_data
        zekr = Zekr.objects.get(pk=data['id'])
        zekr.name = data['name']
        zekr.save()
    return Response(serializer.data)


@api_view(['POST'])
def increment_counter(request):
    tutorial_data = JSONParser().parse(request)
    serializer = IncrementCounterSerializer(data=tutorial_data)
    if serializer.is_valid():
        print("Yes valid")
        data = serializer.validated_data
        zekr = Zekr.objects.get(pk=data['id'])
        zekr.counter += 1 
        zekr.save()
        serializer.data['counter'] = zekr.counter
        newdict={'counter': zekr.counter}
        newdict.update(serializer.data)
    else:
        print("THE ERRORS: ")
        print(serializer.errors)  
    return Response(newdict)

@api_view(['POST'])
def reset_counter(request):
    tutorial_data = JSONParser().parse(request)
    serializer = IncrementCounterSerializer(data=tutorial_data)
    if serializer.is_valid():
        print("Yes valid")
        data = serializer.validated_data
        zekr = Zekr.objects.get(pk=data['id'])
        zekr.counter = 0         
        zekr.save()
        new_dict = {'counter': zekr.counter}
        new_dict.update(serializer.data)
    else:
        print("THE ERRORS: ")
        print(serializer.errors)  
    return Response(new_dict)


@api_view(['POST'])
def try_api(request):
    data_dict = JSONParser().parse(request)
    print(data_dict)
    return Response(data_dict)