"""
    Serializer does in the context of an API is that it translate to and form Json where technically it can be any format you can send over HTTP like you know XML or something like that. 
    But our purposes is going to be json format.
"""

from rest_framework import serializers
from .models import *

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = "__all__"

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = "__all__"

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = "__all__"

class BoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = "__all__"

class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Data
        fields = "__all__"

class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = "__all__"