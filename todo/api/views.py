from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response 
from .serializers import taskSerializer
from .models import task
# Create your views here.

@api_view(['GET'])
def apiOverView(request):
    api_urls={
        'list':'/task-list/',
        'Detail View':'/task-detail/<str:pk>/',
        'Create':'/task-create/',
        'Update':'/task-update/<str:pk>/',
        'Delete':'/task-delete/<str:pk>/'
    }
    return Response(api_urls)

@api_view(['GET'])
def taskList(request):
    tasks=task.objects.all()
    serializer=taskSerializer(tasks,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def taskDetails(request,pk):
    tasks=task.objects.get(id=pk)
    serializer=taskSerializer(tasks,many=False)
    return Response(serializer.data)

@api_view(['POST'])
def taskCreate(request):
    serializer=taskSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
   
    return Response(serializer.data)

@api_view(['POST'])
def taskUpdate(request,pk):
    tasks=task.objects.get(id=pk)
    serializer=taskSerializer(instance=tasks, data=request.data)

    if serializer.is_valid():
        serializer.save()
   
    return Response(serializer.data)

@api_view(['DELETE'])
def taskDelete(request,pk):
    tasks=task.objects.get(id=pk)
    tasks.delete()
   
    return Response('successfully deleted')