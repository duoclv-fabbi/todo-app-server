from rest_framework import serializers
from .models import TaskModel
from django.db import transaction
from utils import exception


class GetAllTodoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskModel
        fields = '__all__'

class CreateTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskModel
        fields = [
            'content'
        ]

    def validate(self, attrs):
        new_content = self.initial_data.get('content')
        if new_content is None or new_content == '':
            raise exception.UserTypeError(detail="wrong type value")

        new_content = TaskModel.objects.filter(content=new_content)
        if new_content.count() > 0:
            raise exception.ExistedValue
        return attrs

    def create(self, validated_data):
        with transaction.atomic():
            instance = TaskModel.objects.create(**validated_data)
            instance.is_complete = False
            instance.save()
            return instance

class UpdateTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskModel
        fields = [
            'id',
            'content',
            'is_complete'
        ]

    def validate(self, attrs):
        return attrs

    def create(self, validated_data):
        with transaction.atomic():
            instance = TaskModel.objects.update(**validated_data)
            return instance

class DeleteTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskModel
        fields = '__all__'

    def validate(self, attrs):
        return attrs

    def update(self, instance, validated_data):
        with transaction.atomic():
            instance.delete()
            return instance

class DeleteAllTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskModel
        fields = '__all__'

    def validate(self, attrs):
        return attrs

    def update(self, instance, validated_data):
        with transaction.atomic():
            TaskModel.objects.all().delete()
            return {}

class CheckAllTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskModel
        fields = '__all__'

    def update(self, instance, validated_data):
        with transaction.atomic():
            TaskModel.objects.all().update(is_complete=True)
            return {}

class RemoveCheckAllTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskModel
        fields = '__all__'

    def validate(self, attrs):
        return attrs

    def update(self, instance, validated_data):
        with transaction.atomic():
            TaskModel.objects.all().update(is_complete=False)
            return {}