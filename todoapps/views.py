from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.parsers import FormParser, MultiPartParser, JSONParser

from utils import exception, permissions, pagination
from .models import TaskModel
from .serializers import GetAllTodoListSerializer, CreateTaskSerializer, UpdateTaskSerializer, DeleteTaskSerializer, DeleteAllTaskSerializer, CheckAllTaskSerializer, RemoveCheckAllTaskSerializer


class GetAllTodoListView(generics.GenericAPIView):
    queryset = TaskModel.objects.all()
    serializer_class = GetAllTodoListSerializer
    authentication_classes = []
    permission_classes = []

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class CreateTaskView(generics.CreateAPIView):
    serializer_class = CreateTaskSerializer
    permission_classes = []
    authentication_classes = []

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        raise exception.APIException()


class UpdateTaskView(generics.GenericAPIView):
    serializer_class = UpdateTaskSerializer
    permission_classes = []
    authentication_classes = []

    def get_object(self):
        pk = self.kwargs['id']
        task = TaskModel.objects.filter(pk=pk)
        if task.count() > 0:
            return task.first()
        raise exception.DoesNotExist(
            detail=f"todo with id {pk} does not exist")

    def put(self, request, *args, **kwargs):
        course = self.get_object()
        serializer = self.get_serializer(course, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        raise exception.APIException()


class DeleteTaskView(generics.DestroyAPIView):
    serializer_class = DeleteTaskSerializer
    queryset = TaskModel.objects.all()
    permission_classes = []

    def get_object(self):
        pk = self.kwargs['id']
        task_delete = TaskModel.objects.filter(id=pk)
        if task_delete.count() > 0:
            return task_delete.first()
        raise exception.DoesNotExist(
            detail=f"task with id {pk} does not exist")

    def delete(self, request, *args, **kwargs):
        obj_delete = self.get_object()
        serializer = self.get_serializer(obj_delete, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(data={}, status=status.HTTP_200_OK)
        raise exception.APIException()


class DeleteAllTaskView(generics.ListAPIView):
    serializer_class = DeleteAllTaskSerializer
    queryset = TaskModel.objects.all()
    permission_classes = []

    def delete(self, request, *args, **kwargs):
        serializer = self.get_serializer({}, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(data={}, status=status.HTTP_200_OK)
        raise exception.APIException()

class RemoveCheckAllTaskView(generics.GenericAPIView):
    serializer_class = RemoveCheckAllTaskSerializer
    permission_classes = []
    authentication_classes = []

    def put(self, request, *args, **kwargs):
        serializer = self.get_serializer({}, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        raise exception.APIException()

class CheckAllTaskView(generics.GenericAPIView):
    serializer_class = CheckAllTaskSerializer
    permission_classes = []
    authentication_classes = []

    def put(self, request, *args, **kwargs):
        serializer = self.get_serializer({}, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        raise exception.APIException()