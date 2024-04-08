from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Todo
from .serializer import TodoSerializer

# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

@api_view(['GET'])
def getTodos(request, id=None):
    if id is None:
        todos = Todo.objects.all()
        serializer = TodoSerializer(todos, many=True)
    else:
        try:
            todo = Todo.objects.get(id=id)
            serializer = TodoSerializer(todo)
        except Todo.DoesNotExist:
            return Response({'error': 'Todo not found'}, status=404)
    return Response(serializer.data)


@api_view(['POST'])
def createTodos(request):
    serializer = TodoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['PUT'])
def updateTodos(request, id):
    try:
        todo = Todo.objects.get(id=id)
    except Todo.DoesNotExist:
        return Response({'error': 'Tarea no encontrada'}, status=404)
    serializer = TodoSerializer(todo, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors, status=400)

@api_view(['DELETE'])
def deleteTodos(request, id):
    try:
        todo = Todo.objects.get(id=id)
    except Todo.DoesNotExist:
        return Response({'error': 'Tarea no encontrada'}, status=404)
    todo.delete()
    return Response({'message': 'Tarea eliminada correctamente'})