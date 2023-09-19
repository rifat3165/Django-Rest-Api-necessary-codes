from django.shortcuts import render
from .models import Aiquest
from .serializer import AiquestSerializer
# from rest_framework.renderers import JSONRenderer
# from django.views.decorators.csrf import csrf_exempt
# import io
# from rest_framework.parsers import JSONParser
# from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response


# Create your views here.(comment)
#Queryset(comment)
# def aiquest_info(request):
#     #complex data(comment)
#     ai = Aiquest.objects.all()
#     #python dict(comment)
#     serializer = AiquestSerializer(ai, many=True)
#     #json render(comment)
#     json_data = JSONRenderer().render(serializer.data)
#     #json data send to user(comment)
#     return HttpResponse(json_data, content_type="application/json")

# #model instance(comment)
# def aiquest_ins(request, pk):
#     #complex data(comment)
#     ai = Aiquest.objects.get(id=pk)
#     #python dict(comment)
#     serializer = AiquestSerializer(ai)
#     #json render(comment)
#     json_data = JSONRenderer().render(serializer.data)
#     #json data send to user(comment)
#     return HttpResponse(json_data, content_type="application.json")


# #deserializer(comment)
# @csrf_exempt
# def aiquest_create(request):
#     if request.method == "POST":
#         json_data = request.body
#         #json to stream convert(comment)
#         stream = io.BytesIO(json_data)
#         #stream to python data(comment)
#         pythondata = JSONParser().parse(stream)
#         #python data to complex data(comment)
#         serializer = AiquestSerializer(data=pythondata)
#         if serializer.is_valid():
#             serializer.save()
#             res = {'msg':'Successfully insert data'}
#             json_data = JSONRenderer().render(res)
#             return HttpResponse(json_data, content_type = 'application.json')
#         json_data = JSONRenderer().render(serializer.errors)
#         return HttpResponse(json_data, content_type = 'application.json')
    
#     if request.method == "PUT":
#         json_data = request.body
#         #json to stream convert(comment)
#         stream = io.BytesIO(json_data)
#         #stream to python data(comment)
#         pythondata = JSONParser().parse(stream)
#         id = pythondata.get('id')
#         aiq = Aiquest.objects.get(id=id)
#         #python data to complex data(comment)
#         serializer = AiquestSerializer(aiq, data=pythondata, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             res = {'msg':'Successfully update data'}
#             json_data = JSONRenderer().render(res)
#             return HttpResponse(json_data, content_type = 'application.json')
#         json_data = JSONRenderer().render(serializer.errors)
#         return HttpResponse(json_data, content_type = 'application.json')

#     if request.method == "DELETE":
#         json_data = request.body
#         #json to stream convert(comment)
#         stream = io.BytesIO(json_data)
#         #stream to python data(comment)
#         pythondata = JSONParser().parse(stream)
#         id = pythondata.get('id')
#         aiq = Aiquest.objects.get(id=id)
#         #python data to complex data(comment)
#         serializer = AiquestSerializer(aiq, data=pythondata)
#         if serializer.is_valid():
#             serializer.save()
#             res = {'msg':'Successfully delete data'}
#             json_data = JSONRenderer().render(res)
#             return HttpResponse(json_data, content_type = 'application.json')
#         json_data = JSONRenderer().render(serializer.errors)
#         return HttpResponse(json_data, content_type = 'application.json')


#api_view
@api_view(['GET', 'POST'])
def aiquest_create(request, pk=None):
    if request.method == 'GET':
        id = pk
        if pk is not None:
            #complex data(comment)
            ai = Aiquest.objects.get(id=id)
            #python dict(comment)
            serializer = AiquestSerializer(ai)
            return Response(serializer.data)
        
        #complex data(comment)
        ai = Aiquest.objects.all()
        #python dict(comment)
        serializer = AiquestSerializer(ai, many=True)
        return Response(serializer.data)
    
    if request.method == "POST":
        serializer = AiquestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg' : 'Succesfully insert data'})

        return Response(serializer.errors)

        