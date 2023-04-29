from rest_framework import serializers
from .models import *

class TopicSERIALIZER(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = "__all__"

class AudioSERIALIZER(serializers.ModelSerializer):
    class Meta:
        model = Audio
        fields = "__all__"

